# coding: utf8
from __future__ import unicode_literals

from spacy.gold import GoldCorpus, json_to_tuple

from spacy.lang.en import English
from spacy.tests.util import make_tempdir


def test_issue4402():
    nlp = English()
    data = json_to_tuple(json_data)
    with make_tempdir() as tmpdir:
        json_file = tmpdir / "test4402.json"
        print(data, file=open(json_file, "w"))
        corpus = GoldCorpus(str(json_file), str(json_file))

        train_docs = corpus.train_docs(nlp, gold_preproc=True, max_length=0)
        # checking that iterating over the training docs works fine
        for text, gold in train_docs:
            pass


json_data = [
    {
        "id": 0,
        "paragraphs": [
            {
                "raw": "How should I cook bacon in an oven?\nI've heard of people cooking bacon in an oven.",
                "sentences": [
                    {
                        "tokens": [
                            {"id": 0, "orth": "How", "ner": "O"},
                            {"id": 1, "orth": "should", "ner": "O"},
                            {"id": 2, "orth": "I", "ner": "O"},
                            {"id": 3, "orth": "cook", "ner": "O"},
                            {"id": 4, "orth": "bacon", "ner": "O"},
                            {"id": 5, "orth": "in", "ner": "O"},
                            {"id": 6, "orth": "an", "ner": "O"},
                            {"id": 7, "orth": "oven", "ner": "O"},
                            {"id": 8, "orth": "?", "ner": "O"},
                        ],
                        "brackets": [],
                    },
                    {
                        "tokens": [
                            {"id": 9, "orth": "\n", "ner": "O"},
                            {"id": 10, "orth": "I", "ner": "O"},
                            {"id": 11, "orth": "'ve", "ner": "O"},
                            {"id": 12, "orth": "heard", "ner": "O"},
                            {"id": 13, "orth": "of", "ner": "O"},
                            {"id": 14, "orth": "people", "ner": "O"},
                            {"id": 15, "orth": "cooking", "ner": "O"},
                            {"id": 16, "orth": "bacon", "ner": "O"},
                            {"id": 17, "orth": "in", "ner": "O"},
                            {"id": 18, "orth": "an", "ner": "O"},
                            {"id": 19, "orth": "oven", "ner": "O"},
                            {"id": 20, "orth": ".", "ner": "O"},
                        ],
                        "brackets": [],
                    },
                ],
                "cats": [
                    {"label": "baking", "value": 1.0},
                    {"label": "not_baking", "value": 0.0},
                ],
            },
            {
                "raw": "What is the difference between white and brown eggs?\n",
                "sentences": [
                    {
                        "tokens": [
                            {"id": 0, "orth": "What", "ner": "O"},
                            {"id": 1, "orth": "is", "ner": "O"},
                            {"id": 2, "orth": "the", "ner": "O"},
                            {"id": 3, "orth": "difference", "ner": "O"},
                            {"id": 4, "orth": "between", "ner": "O"},
                            {"id": 5, "orth": "white", "ner": "O"},
                            {"id": 6, "orth": "and", "ner": "O"},
                            {"id": 7, "orth": "brown", "ner": "O"},
                            {"id": 8, "orth": "eggs", "ner": "O"},
                            {"id": 9, "orth": "?", "ner": "O"},
                        ],
                        "brackets": [],
                    },
                    {"tokens": [{"id": 10, "orth": "\n", "ner": "O"}], "brackets": []},
                ],
                "cats": [
                    {"label": "baking", "value": 0.0},
                    {"label": "not_baking", "value": 1.0},
                ],
            },
        ],
    }
]
