# coding: utf8
from __future__ import unicode_literals

import pytest


GA_TOKEN_EXCEPTION_TESTS = [
    ("B'fhearr fanacht as amharc", ["B'", "fhearr", "fanacht", "as", "amharc"]),
    ('Daoine a bhfuil Gaeilge acu, m.sh. tusa agus mise', ['Daoine', 'a', 'bhfuil', 'Gaeilge', 'acu', ',', 'm.sh.', 'tusa', 'agus', 'mise'])
]


@pytest.mark.parametrize('text,expected_tokens', GA_TOKEN_EXCEPTION_TESTS)
def test_irish_tokeniser(ga_tokenizer, text, expected_tokens):
    tokens = ga_tokenizer(text)
    token_list = [token.text for token in tokens if not token.is_space]
    assert expected_tokens == token_list

