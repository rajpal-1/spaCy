# coding: utf-8
from __future__ import unicode_literals

import pytest
from spacy.vocab import Vocab
from spacy.tokens import Doc

from ..util import get_doc


def test_doc_split(en_vocab):
    words = ["LosAngeles", "start", "."]
    heads = [1, 1, 0]
    doc = get_doc(en_vocab, words=words, heads=heads)
    assert len(doc) == 3
    assert len(str(doc)) == 19
    assert doc[0].head.text == "start"
    assert doc[1].head.text == "."
    with doc.retokenize() as retokenizer:
        retokenizer.split(
            doc[0],
            ["Los", "Angeles"],
            [(doc[0], 1), doc[1]],
            attrs={
                "tag": ["NNP"]*2,
                "lemma": ["Los", "Angeles"],
                "ent_type": ["GPE"]*2
            },
        )
    assert len(doc) == 4
    assert doc[0].text == "Los"
    assert doc[0].head.text == "Angeles"
    assert doc[0].idx == 0
    assert doc[1].idx == 3
    assert doc[1].text == "Angeles"
    assert doc[1].head.text == "start"
    assert doc[2].text == "start"
    assert doc[2].head.text == "."
    assert doc[3].text == "."
    assert doc[3].head.text == "."
    assert len(str(doc)) == 19


def test_split_dependencies(en_vocab):
    doc = Doc(en_vocab, words=["LosAngeles", "start", "."])
    dep1 = doc.vocab.strings.add("amod")
    dep2 = doc.vocab.strings.add("subject")
    with doc.retokenize() as retokenizer:
        retokenizer.split(doc[0], ["Los", "Angeles"],
            [(doc[0], 1), doc[1]], [dep1, dep2])
    assert doc[0].dep == dep1
    assert doc[1].dep == dep2


def test_split_heads_error(en_vocab):
    doc = Doc(en_vocab, words=["LosAngeles", "start", "."])
    # Not enough heads
    with pytest.raises(ValueError):
        with doc.retokenize() as retokenizer:
            retokenizer.split(doc[0], ["Los", "Angeles"], [doc[1]])

    # Too many heads
    with pytest.raises(ValueError):
        with doc.retokenize() as retokenizer:
            retokenizer.split(doc[0], ["Los", "Angeles"], [doc[1], doc[1], doc[1]])


def test_spans_entity_merge_iob():
    # Test entity IOB stays consistent after merging
    words = ["abc", "d", "e"]
    doc = Doc(Vocab(), words=words)
    doc.ents = [(doc.vocab.strings.add("ent-abcd"), 0, 2)]
    assert doc[0].ent_iob_ == "B"
    assert doc[1].ent_iob_ == "I"
    with doc.retokenize() as retokenizer:
        retokenizer.split(doc[0], ["a", "b", "c"],
            [(doc[0], 1), (doc[0], 2), doc[1]])
    assert doc[0].ent_iob_ == "B"
    assert doc[1].ent_iob_ == "I"
    assert doc[2].ent_iob_ == "I"
    assert doc[3].ent_iob_ == "I"


def test_spans_sentence_update_after_merge(en_vocab):
    # fmt: off
    words = ["StewartLee", "is", "a", "stand", "up", "comedian", ".", "He",
             "lives", "in", "England", "and", "loves", "JoePasquale", "."]
    heads = [1, 0, 1, 2, -1, -4, -5, 1, 0, -1, -1, -3, -4, 1, -2]
    deps = ["nsubj", "ROOT", "det", "amod", "prt", "attr", "punct", "nsubj",
            "ROOT", "prep", "pobj", "cc", "conj", "compound", "punct"]
    # fmt: on
    doc = get_doc(en_vocab, words=words, heads=heads, deps=deps)
    sent1, sent2 = list(doc.sents)
    init_len = len(sent1)
    init_len2 = len(sent2)
    with doc.retokenize() as retokenizer:
        retokenizer.split(doc[0], ["Stewart", "Lee"], [(doc[0], 1), doc[1]])
        retokenizer.split(doc[14], ["Joe", "Pasquale"], [(doc[14], 1), doc[13]])
    sent1, sent2 = list(doc.sents)
    assert len(sent1) == init_len + 1
    assert len(sent2) == init_len2 + 1


def test_split_orths_mismatch(en_vocab):
    """Test that the regular retokenizer.split raises an error if the orths
    don't match the original token text. There might still be a method that
    allows this, but for the default use cases, merging and splitting should
    always conform with spaCy's non-destructive tokenization policy. Otherwise,
    it can lead to very confusing and unexpected results.
    """
    doc = Doc(en_vocab, words=["LosAngeles", "start", "."])
    with pytest.raises(ValueError):
        with doc.retokenize() as retokenizer:
            retokenizer.split(doc[0], ["L", "A"], [0, -1])
