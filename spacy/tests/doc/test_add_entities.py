from spacy.gold import Example
from spacy.pipeline import EntityRecognizer
from spacy.tokens import Span, Doc
from spacy import registry
import pytest

from ..util import get_doc
from spacy.pipeline.ner import DEFAULT_NER_MODEL


def _ner_example(ner):
    doc = Doc(ner.vocab, words=["Joe", "loves", "visiting", "London", "during", "the", "weekend"])
    gold = {"entities": [(0, 3, "PERSON"), (19, 25, "LOC")]}
    return Example.from_dict(doc, gold)


def test_doc_add_entities_set_ents_iob(en_vocab):
    text = ["This", "is", "a", "lion"]
    doc = get_doc(en_vocab, text)
    config = {
        "learn_tokens": False,
        "min_action_freq": 30,
        "update_with_oracle_cut_size": 100,
    }
    cfg = {"model": DEFAULT_NER_MODEL}
    model = registry.make_from_config(cfg, validate=True)["model"]
    ner = EntityRecognizer(en_vocab, model, **config)
    ner.begin_training(lambda: [_ner_example(ner)])
    ner(doc)

    doc.ents = [(doc.vocab.strings["ANIMAL"], 3, 4)]
    assert [w.ent_iob_ for w in doc] == ["O", "O", "O", "B"]

    doc.ents = [(doc.vocab.strings["WORD"], 0, 2)]
    assert [w.ent_iob_ for w in doc] == ["B", "I", "O", "O"]


def test_add_overlapping_entities(en_vocab):
    text = ["Louisiana", "Office", "of", "Conservation"]
    doc = get_doc(en_vocab, text)
    entity = Span(doc, 0, 4, label=391)
    doc.ents = [entity]

    new_entity = Span(doc, 0, 1, label=392)
    with pytest.raises(ValueError):
        doc.ents = list(doc.ents) + [new_entity]
