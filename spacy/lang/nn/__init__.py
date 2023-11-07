import spacy
from spacy.language import BaseDefaults, Language
from .punctuation import TOKENIZER_INFIXES, TOKENIZER_PREFIXES, TOKENIZER_SUFFIXES
from spacy.lang.nb import SYNTAX_ITERATORS
from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS


class NorwegianNynorskDefaults(BaseDefaults):
    tokenizer_exceptions = TOKENIZER_EXCEPTIONS
    prefixes = TOKENIZER_PREFIXES
    infixes = TOKENIZER_INFIXES
    suffixes = TOKENIZER_SUFFIXES
    syntax_iterators = SYNTAX_ITERATORS


@spacy.registry.languages("nn")
class NorwegianNynorsk(Language):
    lang = "nn"
    Defaults = NorwegianNynorskDefaults


__all__ = ["Norwegian"]
