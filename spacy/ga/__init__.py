from __future__ import unicode_literals, print_function

from os import path

from ..language import Language
from ..attrs import LANG

# Import language-specific data
from .language_data import *

class Irish(Language):
    lang = 'ga' # ISO code

    class Defaults(Language.Defaults):
        lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
        lex_attr_getters[LANG] = lambda text: 'ga'

        stop_words = STOP_WORDS
        tokenizer_exceptions = TOKENIZER_EXCEPTIONS
