#!/usr/bin/env python
# coding: utf8

"""Example of training spaCy's entity linker, starting off with an
existing model or a blank model with a pre-defined knowledge base.

For more details, see the documentation:
* Training: https://spacy.io/usage/training
* NER: https://spacy.io/usage/linguistic-features#entity-linking

Compatible with: spaCy vX.X
Last tested with: vX.X
"""
from __future__ import unicode_literals, print_function

import plac
import random
from pathlib import Path

from spacy.symbols import PERSON
from spacy.vocab import Vocab

import spacy
from spacy.kb import KnowledgeBase

from spacy import Errors
from spacy.tokens import Span
from spacy.util import minibatch, compounding


def sample_train_data():
    train_data = []

    # Q2146908 (Russ Cochran): American golfer
    # Q7381115 (Russ Cochran): publisher

    text_1 = "Russ Cochran's reprints include The Complete EC Library."
    dict_1 = {(0, 12): {"Q7381115": True, "Q2146908": False}}
    train_data.append((text_1, {"links": dict_1}))

    text_2 = "Russ Cochran has been publishing comic art."
    dict_2 = {(0, 12): {"Q7381115": True, "Q2146908": False}}
    train_data.append((text_2, {"links": dict_2}))

    text_3 = "Russ Cochran captured his first major title with his son as caddie."
    dict_3 = {(0, 12): {"Q7381115": False, "Q2146908": True}}
    train_data.append((text_3, {"links": dict_3}))

    text_4 = "Russ Cochran was a member of University of Kentucky's golf team."
    dict_4 = {(0, 12): {"Q7381115": False, "Q2146908": True}}
    train_data.append((text_4, {"links": dict_4}))

    return train_data


# training data
TRAIN_DATA = sample_train_data()


@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    kb_path=("Path to the knowledge base", "option", "kb", Path),
    vocab_path=("Path to the vocab", "option", "v", Path),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int),
)
def main(model=None, kb_path=None, vocab_path=None, output_dir=None, n_iter=1000):
    """Load the model, set up the pipeline and train the entity linker."""
    if model is None and (kb_path is None or vocab_path is None):
        raise ValueError(Errors.E150)

    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        vocab = nlp.vocab
        print("Loaded model '%s'" % model)
    else:
        vocab = Vocab().from_disk(vocab_path)
        nlp = spacy.blank("en", vocab=vocab)  # create blank Language class
        nlp.vocab.vectors.name = "spacy_pretrained_vectors"
        print("Created blank 'en' model with pre-defined vocab")

    # create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if "entity_linker" not in nlp.pipe_names:
        entity_linker = nlp.create_pipe("entity_linker")
        kb = KnowledgeBase(vocab=vocab)
        kb.load_bulk(kb_path)
        print("Loaded Knowledge Base")
        entity_linker.set_kb(kb)
        nlp.add_pipe(entity_linker, last=True)
    else:
        entity_linker = nlp.get_pipe("entity_linker")
        kb = entity_linker.kb

    # make sure the annotated examples correspond to known identifiers in the knowlege base
    kb_ids = kb.get_entity_strings()
    for text, annotation in TRAIN_DATA:
        for offset, kb_id_dict in annotation["links"].items():
            new_dict = {}
            for kb_id, value in kb_id_dict.items():
                if kb_id in kb_ids:
                    new_dict[kb_id] = value
                else:
                    print(
                        "Removed",
                        kb_id,
                        "from the training data because it is not in the KB.",
                    )
            annotation["links"][offset] = new_dict

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "entity_linker"]
    with nlp.disable_pipes(*other_pipes):  # only train entity linker
        # reset and initialize the weights randomly – but only if we're
        # training a new model
        if model is None:
            nlp.begin_training()
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}
            # batch up the examples using spaCy's minibatch
            batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(
                    texts,  # batch of texts
                    annotations,  # batch of annotations
                    drop=0.5,  # dropout - make it harder to memorise data
                    losses=losses,
                )
            print("Losses", losses)

    # test the trained model
    for text, annotation in TRAIN_DATA:
        doc = nlp(text)

        # set entities so the evaluation is independent of the NER step
        # all the examples contain Russ Cochran as the first two tokens in the sentence
        rc_ent = Span(doc, 0, 2, label=PERSON)
        doc.ents = [rc_ent]

        # re-apply the entity linker which will now make predictions for the entities
        doc = entity_linker(doc)

        print("Entities", [(ent.text, ent.label_, ent.kb_id_) for ent in doc.ents])
        print("Tokens", [(t.text, t.ent_type_, t.ent_kb_id_) for t in doc])
        print()

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        for text, annotation in TRAIN_DATA:
            doc = nlp2(text)

            # set entities so the evaluation is independent of the NER step
            # all the examples contain Russ Cochran as the first two tokens in the sentence
            rc_ent = Span(doc, 0, 2, label=PERSON)
            doc.ents = [rc_ent]

            # re-apply the entity linker which will now make predictions for the entities
            doc = entity_linker(doc)

            print("Entities", [(ent.text, ent.label_, ent.kb_id_) for ent in doc.ents])
            print("Tokens", [(t.text, t.ent_type_, t.ent_kb_id_) for t in doc])
            print()


if __name__ == "__main__":
    plac.call(main)

    # Expected output:

    # Entities[('Russ Cochran', 'PERSON', 'Q7381115')]
    # Tokens[('Russ', 'PERSON', 'Q7381115'), ('Cochran', 'PERSON', 'Q7381115'), ("'s", '', ''), ('reprints', '', ''), ('include', '', ''), ('The', '', ''), ('Complete', '', ''), ('EC', '', ''), ('Library', '', ''), ('.', '', '')]

    # Entities[('Russ Cochran', 'PERSON', 'Q7381115')]
    # Tokens[('Russ', 'PERSON', 'Q7381115'), ('Cochran', 'PERSON', 'Q7381115'), ('has', '', ''), ('been', '', ''), ('publishing', '', ''), ('comic', '', ''), ('art', '', ''), ('.', '', '')]

    # Entities[('Russ Cochran', 'PERSON', 'Q2146908')]
    # Tokens[('Russ', 'PERSON', 'Q2146908'), ('Cochran', 'PERSON', 'Q2146908'), ('captured', '', ''), ('his', '', ''), ('first', '', ''), ('major', '', ''), ('title', '', ''), ('with', '', ''), ('his', '', ''), ('son', '', ''), ('as', '', ''), ('caddie', '', ''), ('.', '', '')]

    # Entities[('Russ Cochran', 'PERSON', 'Q2146908')]
    # Tokens[('Russ', 'PERSON', 'Q2146908'), ('Cochran', 'PERSON', 'Q2146908'), ('was', '', ''), ('a', '', ''), ('member', '', ''), ('of', '', ''), ('University', '', ''), ('of', '', ''), ('Kentucky', '', ''), ("'s", '', ''), ('golf', '', ''), ('team', '', ''), ('.', '', '')]
