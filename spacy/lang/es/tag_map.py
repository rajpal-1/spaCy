# coding: utf8
from __future__ import unicode_literals

from ...symbols import POS, PUNCT, SYM, ADJ, NUM, DET, ADV, ADP, X, VERB
from ...symbols import NOUN, PROPN, PART, INTJ, SPACE, PRON, SCONJ, AUX, CONJ

# fmt: off
TAG_MAP = {
    "ADJ___": {"morph": "_", POS: ADJ},
    "ADJ__AdpType=Prep": {"morph": "AdpType=Prep", POS: ADJ},
    "ADJ__AdpType=Preppron|Gender=Masc|Number=Sing": {"morph": "AdpType=Preppron|Gender=Masc|Number=Sing", POS: ADV},
    "ADJ__AdvType=Tim": {"morph": "AdvType=Tim", POS: ADJ},
    "ADJ__Gender=Fem|Number=Plur": {"morph": "Gender=Fem|Number=Plur", POS: ADJ},
    "ADJ__Gender=Fem|Number=Plur|NumType=Ord": {"morph": "Gender=Fem|Number=Plur|NumType=Ord", POS: ADJ},
    "ADJ__Gender=Fem|Number=Plur|VerbForm=Part": {"morph": "Gender=Fem|Number=Plur|VerbForm=Part", POS: ADJ},
    "ADJ__Gender=Fem|Number=Sing": {"morph": "Gender=Fem|Number=Sing", POS: ADJ},
    "ADJ__Gender=Fem|Number=Sing|NumType=Ord": {"morph": "Gender=Fem|Number=Sing|NumType=Ord", POS: ADJ},
    "ADJ__Gender=Fem|Number=Sing|VerbForm=Part": {"morph": "Gender=Fem|Number=Sing|VerbForm=Part", POS: ADJ},
    "ADJ__Gender=Masc": {"morph": "Gender=Masc", POS: ADJ},
    "ADJ__Gender=Masc|Number=Plur": {"morph": "Gender=Masc|Number=Plur", POS: ADJ},
    "ADJ__Gender=Masc|Number=Plur|NumType=Ord": {"morph": "Gender=Masc|Number=Plur|NumType=Ord", POS: ADJ},
    "ADJ__Gender=Masc|Number=Plur|VerbForm=Part": {"morph": "Gender=Masc|Number=Plur|VerbForm=Part", POS: ADJ},
    "ADJ__Gender=Masc|Number=Sing": {"morph": "Gender=Masc|Number=Sing", POS: ADJ},
    "ADJ__Gender=Masc|Number=Sing|NumType=Ord": {"morph": "Gender=Masc|Number=Sing|NumType=Ord", POS: ADJ},
    "ADJ__Gender=Masc|Number=Sing|VerbForm=Part": {"morph": "Gender=Masc|Number=Sing|VerbForm=Part", POS: ADJ},
    "ADJ__Number=Plur": {"morph": "Number=Plur", POS: ADJ},
    "ADJ__Number=Sing": {"morph": "Number=Sing", POS: ADJ},
    "ADP__AdpType=Prep": {"morph": "AdpType=Prep", POS: ADP},
    "ADP__AdpType=Preppron|Gender=Fem|Number=Sing": {"morph": "AdpType=Preppron|Gender=Fem|Number=Sing", POS: ADP},
    "ADP__AdpType=Preppron|Gender=Masc|Number=Plur": {"morph": "AdpType=Preppron|Gender=Masc|Number=Plur", POS: ADP},
    "ADP__AdpType=Preppron|Gender=Masc|Number=Sing": {"morph": "AdpType=Preppron|Gender=Masc|Number=Sing", POS: ADP},
    "ADP": {POS: ADP},
    "ADV___": {"morph": "_", POS: ADV},
    "ADV__AdpType=Prep": {"morph": "AdpType=Prep", POS: ADV},
    "ADV__AdpType=Preppron|Gender=Masc|Number=Sing": {"morph": "AdpType=Preppron|Gender=Masc|Number=Sing", POS: ADV},
    "ADV__AdvType=Tim": {"morph": "AdvType=Tim", POS: ADV},
    "ADV__Gender=Masc|Number=Sing": {"morph": "Gender=Masc|Number=Sing", POS: ADV},
    "ADV__Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin", POS: ADV},
    "ADV__Negative=Neg": {"morph": "Negative=Neg", POS: ADV},
    "ADV__Number=Plur": {"morph": "Number=Plur", POS: ADV},
    "ADV__Polarity=Neg": {"morph": "Polarity=Neg", POS: ADV},
    "AUX__Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part": {"morph": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part", POS: AUX},
    "AUX__Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part": {"morph": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part", POS: AUX},
    "AUX__Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part": {"morph": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part", POS: AUX},
    "AUX__Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part": {"morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part", POS: AUX},
    "AUX__Mood=Cnd|Number=Plur|Person=1|VerbForm=Fin": {"morph": "Mood=Cnd|Number=Plur|Person=1|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Cnd|Number=Plur|Person=3|VerbForm=Fin": {"morph": "Mood=Cnd|Number=Plur|Person=3|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Cnd|Number=Sing|Person=1|VerbForm=Fin": {"morph": "Mood=Cnd|Number=Sing|Person=1|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Cnd|Number=Sing|Person=2|VerbForm=Fin": {"morph": "Mood=Cnd|Number=Sing|Person=2|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Cnd|Number=Sing|Person=3|VerbForm=Fin": {"morph": "Mood=Cnd|Number=Sing|Person=3|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Imp|Number=Plur|Person=3|VerbForm=Fin": {"morph": "Mood=Imp|Number=Plur|Person=3|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Imp|Number=Sing|Person=2|VerbForm=Fin": {"morph": "Mood=Imp|Number=Sing|Person=2|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Imp|Number=Sing|Person=3|VerbForm=Fin": {"morph": "Mood=Imp|Number=Sing|Person=3|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Plur|Person=1|Tense=Fut|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=1|Tense=Fut|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Plur|Person=1|Tense=Past|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=1|Tense=Past|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Plur|Person=3|Tense=Past|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=3|Tense=Past|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Sing|Person=1|Tense=Fut|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=1|Tense=Fut|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Sing|Person=1|Tense=Past|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=1|Tense=Past|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Sing|Person=2|Tense=Fut|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=2|Tense=Fut|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Sing|Person=2|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=2|Tense=Imp|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Sub|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Sub|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Sub|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Sub|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Sub|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Sub|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Sub|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Sub|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Sub|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Sub|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Sub|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Sub|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Sub|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Sub|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Sub|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Sub|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin", POS: AUX},
    "AUX__Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin", POS: AUX},
    "AUX__VerbForm=Ger": {"morph": "VerbForm=Ger", POS: AUX},
    "AUX__VerbForm=Inf": {"morph": "VerbForm=Inf", POS: AUX},
    "CCONJ___": {"morph": "_", POS: CONJ},
    "CONJ___": {"morph": "_", POS: CONJ},
    "DET__Definite=Def|Gender=Fem|Number=Plur|PronType=Art": {"morph": "Definite=Def|Gender=Fem|Number=Plur|PronType=Art", POS: DET},
    "DET__Definite=Def|Gender=Fem|Number=Sing|PronType=Art": {"morph": "Definite=Def|Gender=Fem|Number=Sing|PronType=Art", POS: DET},
    "DET__Definite=Def|Gender=Masc|Number=Plur|PronType=Art": {"morph": "Definite=Def|Gender=Masc|Number=Plur|PronType=Art", POS: DET},
    "DET__Definite=Def|Gender=Masc|Number=Sing|PronType=Art": {"morph": "Definite=Def|Gender=Masc|Number=Sing|PronType=Art", POS: DET},
    "DET__Definite=Def|Gender=Masc|PronType=Art": {"morph": "Definite=Def|Gender=Masc|PronType=Art", POS: DET},
    "DET__Definite=Def|Number=Sing|PronType=Art": {"morph": "Definite=Def|Number=Sing|PronType=Art", POS: DET},
    "DET__Definite=Ind|Gender=Fem|Number=Plur|PronType=Art": {"morph": "Definite=Ind|Gender=Fem|Number=Plur|PronType=Art", POS: DET},
    "DET__Definite=Ind|Gender=Fem|Number=Sing|NumType=Card|PronType=Art": {"morph": "Definite=Ind|Gender=Fem|Number=Sing|NumType=Card|PronType=Art", POS: DET},
    "DET__Definite=Ind|Gender=Fem|Number=Sing|PronType=Art": {"morph": "Definite=Ind|Gender=Fem|Number=Sing|PronType=Art", POS: DET},
    "DET__Definite=Ind|Gender=Masc|Number=Plur|PronType=Art": {"morph": "Definite=Ind|Gender=Masc|Number=Plur|PronType=Art", POS: DET},
    "DET__Definite=Ind|Gender=Masc|Number=Sing|NumType=Card|PronType=Art": {"morph": "Definite=Ind|Gender=Masc|Number=Sing|NumType=Card|PronType=Art", POS: DET},
    "DET__Definite=Ind|Gender=Masc|Number=Sing|PronType=Art": {"morph": "Definite=Ind|Gender=Masc|Number=Sing|PronType=Art", POS: DET},
    "DET__Gender=Fem|Number=Plur|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs": {"morph": "Gender=Fem|Number=Plur|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Gender=Fem|Number=Plur|Number[psor]=Plur|Person=2|Poss=Yes|PronType=Prs": {"morph": "Gender=Fem|Number=Plur|Number[psor]=Plur|Person=2|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Gender=Fem|Number=Plur|Person=3|Poss=Yes|PronType=Prs": {"morph": "Gender=Fem|Number=Plur|Person=3|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Gender=Fem|Number=Plur|PronType=Art": {"morph": "Gender=Fem|Number=Plur|PronType=Art", POS: DET},
    "DET__Gender=Fem|Number=Plur|PronType=Dem": {"morph": "Gender=Fem|Number=Plur|PronType=Dem", POS: DET},
    "DET__Gender=Fem|Number=Plur|PronType=Ind": {"morph": "Gender=Fem|Number=Plur|PronType=Ind", POS: DET},
    "DET__Gender=Fem|Number=Sing|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs": {"morph": "Gender=Fem|Number=Sing|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Gender=Fem|Number=Sing|Number[psor]=Plur|Person=2|Poss=Yes|PronType=Prs": {"morph": "Gender=Fem|Number=Sing|Number[psor]=Plur|Person=2|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Gender=Fem|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs": {"morph": "Gender=Fem|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Gender=Fem|Number=Sing|Person=3|Poss=Yes|PronType=Prs": {"morph": "Gender=Fem|Number=Sing|Person=3|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Gender=Fem|Number=Sing|PronType=Art": {"morph": "Gender=Fem|Number=Sing|PronType=Art", POS: DET},
    "DET__Gender=Fem|Number=Sing|PronType=Dem": {"morph": "Gender=Fem|Number=Sing|PronType=Dem", POS: DET},
    "DET__Gender=Fem|Number=Sing|PronType=Ind": {"morph": "Gender=Fem|Number=Sing|PronType=Ind", POS: DET},
    "DET__Gender=Fem|Number=Sing|PronType=Int": {"morph": "Gender=Fem|Number=Sing|PronType=Int", POS: DET},
    "DET__Gender=Masc|Number=Plur|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs": {"morph": "Gender=Masc|Number=Plur|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Gender=Masc|Number=Plur|Person=3|Poss=Yes|PronType=Prs": {"morph": "Gender=Masc|Number=Plur|Person=3|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Gender=Masc|Number=Plur|PronType=Art": {"morph": "Gender=Masc|Number=Plur|PronType=Art", POS: DET},
    "DET__Gender=Masc|Number=Plur|PronType=Dem": {"morph": "Gender=Masc|Number=Plur|PronType=Dem", POS: DET},
    "DET__Gender=Masc|Number=Plur|PronType=Ind": {"morph": "Gender=Masc|Number=Plur|PronType=Ind", POS: DET},
    "DET__Gender=Masc|Number=Sing|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs": {"morph": "Gender=Masc|Number=Sing|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Gender=Masc|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs": {"morph": "Gender=Masc|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Gender=Masc|Number=Sing|Person=3|Poss=Yes|PronType=Prs": {"morph": "Gender=Masc|Number=Sing|Person=3|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Gender=Masc|Number=Sing|PronType=Art": {"morph": "Gender=Masc|Number=Sing|PronType=Art", POS: DET},
    "DET__Gender=Masc|Number=Sing|PronType=Dem": {"morph": "Gender=Masc|Number=Sing|PronType=Dem", POS: DET},
    "DET__Gender=Masc|Number=Sing|PronType=Ind": {"morph": "Gender=Masc|Number=Sing|PronType=Ind", POS: DET},
    "DET__Gender=Masc|Number=Sing|PronType=Int": {"morph": "Gender=Masc|Number=Sing|PronType=Int", POS: DET},
    "DET__Gender=Masc|Number=Sing|PronType=Tot": {"morph": "Gender=Masc|Number=Sing|PronType=Tot", POS: DET},
    "DET__Number=Plur|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs": {"morph": "Number=Plur|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Number=Plur|Number[psor]=Sing|Person=2|Poss=Yes|PronType=Prs": {"morph": "Number=Plur|Number[psor]=Sing|Person=2|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Number=Plur|Person=3|Poss=Yes|PronType=Prs": {"morph": "Number=Plur|Person=3|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Number=Plur|PronType=Dem": {"morph": "Number=Plur|PronType=Dem", POS: DET},
    "DET__Number=Plur|PronType=Ind": {"morph": "Number=Plur|PronType=Ind", POS: DET},
    "DET__Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs": {"morph": "Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Number=Sing|Number[psor]=Sing|Person=2|Poss=Yes|PronType=Prs": {"morph": "Number=Sing|Number[psor]=Sing|Person=2|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Number=Sing|Person=3|Poss=Yes|PronType=Prs": {"morph": "Number=Sing|Person=3|Poss=Yes|PronType=Prs", POS: DET},
    "DET__Number=Sing|PronType=Dem": {"morph": "Number=Sing|PronType=Dem", POS: DET},
    "DET__Number=Sing|PronType=Ind": {"morph": "Number=Sing|PronType=Ind", POS: DET},
    "DET__PronType=Int": {"morph": "PronType=Int", POS: DET},
    "DET__PronType=Rel": {"morph": "PronType=Rel", POS: DET},
    "DET": {POS: DET},
    "INTJ___": {"morph": "_", POS: INTJ},
    "NOUN___": {"morph": "_", POS: NOUN},
    "NOUN__AdvType=Tim": {"morph": "AdvType=Tim", POS: NOUN},
    "NOUN__AdvType=Tim|Gender=Masc|Number=Sing": {"morph": "AdvType=Tim|Gender=Masc|Number=Sing", POS: NOUN},
    "NOUN__Gender=Fem": {"morph": "Gender=Fem", POS: NOUN},
    "NOUN__Gender=Fem|Number=Plur": {"morph": "Gender=Fem|Number=Plur", POS: NOUN},
    "NOUN__Gender=Fem|Number=Sing": {"morph": "Gender=Fem|Number=Sing", POS: NOUN},
    "NOUN__Gender=Masc": {"morph": "Gender=Masc", POS: NOUN},
    "NOUN__Gender=Masc|Number=Plur": {"morph": "Gender=Masc|Number=Plur", POS: NOUN},
    "NOUN__Gender=Masc|Number=Sing": {"morph": "Gender=Masc|Number=Sing", POS: NOUN},
    "NOUN__Gender=Masc|Number=Sing|VerbForm=Part": {"morph": "Gender=Masc|Number=Sing|VerbForm=Part", POS: NOUN},
    "NOUN__Number=Plur": {"morph": "Number=Plur", POS: NOUN},
    "NOUN__Number=Sing": {"morph": "Number=Sing", POS: NOUN},
    "NOUN__NumForm=Digit": {"morph": "NumForm=Digit", POS: NOUN},
    "NUM__Gender=Fem|Number=Plur|NumType=Card": {"morph": "Gender=Fem|Number=Plur|NumType=Card", POS: NUM},
    "NUM__Gender=Fem|Number=Sing|NumType=Card": {"morph": "Gender=Fem|Number=Sing|NumType=Card", POS: NUM},
    "NUM__Gender=Masc|Number=Plur|NumType=Card": {"morph": "Gender=Masc|Number=Plur|NumType=Card", POS: NUM},
    "NUM__Gender=Masc|Number=Sing|NumType=Card": {"morph": "Gender=Masc|Number=Sing|NumType=Card", POS: NUM},
    "NUM__Number=Plur|NumType=Card": {"morph": "Number=Plur|NumType=Card", POS: NUM},
    "NUM__Number=Sing|NumType=Card": {"morph": "Number=Sing|NumType=Card", POS: NUM},
    "NUM__NumForm=Digit": {"morph": "NumForm=Digit", POS: NUM},
    "NUM__NumForm=Digit|NumType=Card": {"morph": "NumForm=Digit|NumType=Card", POS: NUM},
    "NUM__NumForm=Digit|NumType=Frac": {"morph": "NumForm=Digit|NumType=Frac", POS: NUM},
    "NUM__NumType=Card": {"morph": "NumType=Card", POS: NUM},
    "PART___": {"morph": "_", POS: PART},
    "PART__Negative=Neg": {"morph": "Negative=Neg", POS: PART},
    "PRON___": {"morph": "_", POS: PRON},
    "PRON__Case=Acc|Gender=Fem|Number=Plur|Person=3|PronType=Prs": {"morph": "Case=Acc|Gender=Fem|Number=Plur|Person=3|PronType=Prs", POS: PRON},
    "PRON__Case=Acc|Gender=Fem|Number=Sing|Person=3|PronType=Prs": {"morph": "Case=Acc|Gender=Fem|Number=Sing|Person=3|PronType=Prs", POS: PRON},
    "PRON__Case=Acc|Gender=Masc|Number=Plur|Person=3|PronType=Prs": {"morph": "Case=Acc|Gender=Masc|Number=Plur|Person=3|PronType=Prs", POS: PRON},
    "PRON__Case=Acc|Gender=Masc|Number=Sing|Person=3|PronType=Prs": {"morph": "Case=Acc|Gender=Masc|Number=Sing|Person=3|PronType=Prs", POS: PRON},
    "PRON__Case=Acc|Number=Plur|Person=3|PronType=Prs": {"morph": "Case=Acc|Number=Plur|Person=3|PronType=Prs", POS: PRON},
    "PRON__Case=Acc|Number=Sing|Person=3|PronType=Prs": {"morph": "Case=Acc|Number=Sing|Person=3|PronType=Prs", POS: PRON},
    "PRON__Case=Acc|Person=3|PronType=Prs": {"morph": "Case=Acc|Person=3|PronType=Prs", POS: PRON},
    "PRON__Case=Dat|Number=Plur|Person=3|PronType=Prs": {"morph": "Case=Dat|Number=Plur|Person=3|PronType=Prs", POS: PRON},
    "PRON__Case=Dat|Number=Sing|Person=3|PronType=Prs": {"morph": "Case=Dat|Number=Sing|Person=3|PronType=Prs", POS: PRON},
    "PRON__Case=Nom|Number=Sing|Person=1|PronType=Prs": {"morph": "Case=Nom|Number=Sing|Person=1|PronType=Prs", POS: PRON},
    "PRON__Case=Nom|Number=Sing|Person=2|PronType=Prs": {"morph": "Case=Nom|Number=Sing|Person=2|PronType=Prs", POS: PRON},
    "PRON__Gender=Fem|Number=Plur|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs": {"morph": "Gender=Fem|Number=Plur|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs", POS: PRON},
    "PRON__Gender=Fem|Number=Plur|Person=3|Poss=Yes|PronType=Prs": {"morph": "Gender=Fem|Number=Plur|Person=3|Poss=Yes|PronType=Prs", POS: PRON},
    "PRON__Gender=Fem|Number=Plur|Person=3|PronType=Prs": {"morph": "Gender=Fem|Number=Plur|Person=3|PronType=Prs", POS: PRON},
    "PRON__Gender=Fem|Number=Plur|PronType=Dem": {"morph": "Gender=Fem|Number=Plur|PronType=Dem", POS: PRON},
    "PRON__Gender=Fem|Number=Plur|PronType=Ind": {"morph": "Gender=Fem|Number=Plur|PronType=Ind", POS: PRON},
    "PRON__Gender=Fem|Number=Plur|PronType=Int": {"morph": "Gender=Fem|Number=Plur|PronType=Int", POS: PRON},
    "PRON__Gender=Fem|Number=Plur|PronType=Rel": {"morph": "Gender=Fem|Number=Plur|PronType=Rel", POS: PRON},
    "PRON__Gender=Fem|Number=Sing|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs": {"morph": "Gender=Fem|Number=Sing|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs", POS: PRON},
    "PRON__Gender=Fem|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs": {"morph": "Gender=Fem|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs", POS: PRON},
    "PRON__Gender=Fem|Number=Sing|Number[psor]=Sing|Person=2|Poss=Yes|PronType=Prs": {"morph": "Gender=Fem|Number=Sing|Number[psor]=Sing|Person=2|Poss=Yes|PronType=Prs", POS: PRON},
    "PRON__Gender=Fem|Number=Sing|Person=1|PronType=Prs": {"morph": "Gender=Fem|Number=Sing|Person=1|PronType=Prs", POS: PRON},
    "PRON__Gender=Fem|Number=Sing|Person=3|Poss=Yes|PronType=Prs": {"morph": "Gender=Fem|Number=Sing|Person=3|Poss=Yes|PronType=Prs", POS: PRON},
    "PRON__Gender=Fem|Number=Sing|Person=3|PronType=Prs": {"morph": "Gender=Fem|Number=Sing|Person=3|PronType=Prs", POS: PRON},
    "PRON__Gender=Fem|Number=Sing|PronType=Dem": {"morph": "Gender=Fem|Number=Sing|PronType=Dem", POS: PRON},
    "PRON__Gender=Fem|Number=Sing|PronType=Ind": {"morph": "Gender=Fem|Number=Sing|PronType=Ind", POS: PRON},
    "PRON__Gender=Fem|Number=Sing|PronType=Rel": {"morph": "Gender=Fem|Number=Sing|PronType=Rel", POS: PRON},
    "PRON__Gender=Masc|Number=Plur|Person=1|PronType=Prs": {"morph": "Gender=Masc|Number=Plur|Person=1|PronType=Prs", POS: PRON},
    "PRON__Gender=Masc|Number=Plur|Person=2|Poss=Yes|PronType=Prs": {"morph": "Gender=Masc|Number=Plur|Person=2|Poss=Yes|PronType=Prs", POS: PRON},
    "PRON__Gender=Masc|Number=Plur|Person=3|PronType=Prs": {"morph": "Gender=Masc|Number=Plur|Person=3|PronType=Prs", POS: PRON},
    "PRON__Gender=Masc|Number=Plur|PronType=Dem": {"morph": "Gender=Masc|Number=Plur|PronType=Dem", POS: PRON},
    "PRON__Gender=Masc|Number=Plur|PronType=Ind": {"morph": "Gender=Masc|Number=Plur|PronType=Ind", POS: PRON},
    "PRON__Gender=Masc|Number=Plur|PronType=Int": {"morph": "Gender=Masc|Number=Plur|PronType=Int", POS: PRON},
    "PRON__Gender=Masc|Number=Plur|PronType=Rel": {"morph": "Gender=Masc|Number=Plur|PronType=Rel", POS: PRON},
    "PRON__Gender=Masc|Number=Sing|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs": {"morph": "Gender=Masc|Number=Sing|Number[psor]=Plur|Person=1|Poss=Yes|PronType=Prs", POS: PRON},
    "PRON__Gender=Masc|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs": {"morph": "Gender=Masc|Number=Sing|Number[psor]=Sing|Person=1|Poss=Yes|PronType=Prs", POS: PRON},
    "PRON__Gender=Masc|Number=Sing|Number[psor]=Sing|Person=2|Poss=Yes|PronType=Prs": {"morph": "Gender=Masc|Number=Sing|Number[psor]=Sing|Person=2|Poss=Yes|PronType=Prs", POS: PRON},
    "PRON__Gender=Masc|Number=Sing|Person=3|Poss=Yes|PronType=Prs": {"morph": "Gender=Masc|Number=Sing|Person=3|Poss=Yes|PronType=Prs", POS: PRON},
    "PRON__Gender=Masc|Number=Sing|Person=3|PronType=Prs": {"morph": "Gender=Masc|Number=Sing|Person=3|PronType=Prs", POS: PRON},
    "PRON__Gender=Masc|Number=Sing|PronType=Dem": {"morph": "Gender=Masc|Number=Sing|PronType=Dem", POS: PRON},
    "PRON__Gender=Masc|Number=Sing|PronType=Ind": {"morph": "Gender=Masc|Number=Sing|PronType=Ind", POS: PRON},
    "PRON__Gender=Masc|Number=Sing|PronType=Int": {"morph": "Gender=Masc|Number=Sing|PronType=Int", POS: PRON},
    "PRON__Gender=Masc|Number=Sing|PronType=Rel": {"morph": "Gender=Masc|Number=Sing|PronType=Rel", POS: PRON},
    "PRON__Gender=Masc|Number=Sing|PronType=Tot": {"morph": "Gender=Masc|Number=Sing|PronType=Tot", POS: PRON},
    "PRON__Number=Plur|Person=1": {"morph": "Number=Plur|Person=1", POS: PRON},
    "PRON__Number=Plur|Person=1|PronType=Prs": {"morph": "Number=Plur|Person=1|PronType=Prs", POS: PRON},
    "PRON__Number=Plur|Person=2|Polite=Form|PronType=Prs": {"morph": "Number=Plur|Person=2|Polite=Form|PronType=Prs", POS: PRON},
    "PRON__Number=Plur|Person=2|PronType=Prs": {"morph": "Number=Plur|Person=2|PronType=Prs", POS: PRON},
    "PRON__Number=Plur|Person=3|Poss=Yes|PronType=Prs": {"morph": "Number=Plur|Person=3|Poss=Yes|PronType=Prs", POS: PRON},
    "PRON__Number=Plur|Person=3|PronType=Prs": {"morph": "Number=Plur|Person=3|PronType=Prs", POS: PRON},
    "PRON__Number=Plur|PronType=Dem": {"morph": "Number=Plur|PronType=Dem", POS: PRON},
    "PRON__Number=Plur|PronType=Ind": {"morph": "Number=Plur|PronType=Ind", POS: PRON},
    "PRON__Number=Plur|PronType=Int": {"morph": "Number=Plur|PronType=Int", POS: PRON},
    "PRON__Number=Plur|PronType=Rel": {"morph": "Number=Plur|PronType=Rel", POS: PRON},
    "PRON__Number=Sing|Person=1": {"morph": "Number=Sing|Person=1", POS: PRON},
    "PRON__Number=Sing|Person=1|PrepCase=Pre|PronType=Prs": {"morph": "Number=Sing|Person=1|PrepCase=Pre|PronType=Prs", POS: PRON},
    "PRON__Number=Sing|Person=1|PronType=Prs": {"morph": "Number=Sing|Person=1|PronType=Prs", POS: PRON},
    "PRON__Number=Sing|Person=2": {"morph": "Number=Sing|Person=2", POS: PRON},
    "PRON__Number=Sing|Person=2|Polite=Form|PronType=Prs": {"morph": "Number=Sing|Person=2|Polite=Form|PronType=Prs", POS: PRON},
    "PRON__Number=Sing|Person=2|PrepCase=Pre|PronType=Prs": {"morph": "Number=Sing|Person=2|PrepCase=Pre|PronType=Prs", POS: PRON},
    "PRON__Number=Sing|Person=2|PronType=Prs": {"morph": "Number=Sing|Person=2|PronType=Prs", POS: PRON},
    "PRON__Number=Sing|Person=3|Poss=Yes|PronType=Prs": {"morph": "Number=Sing|Person=3|Poss=Yes|PronType=Prs", POS: PRON},
    "PRON__Number=Sing|Person=3|PronType=Prs": {"morph": "Number=Sing|Person=3|PronType=Prs", POS: PRON},
    "PRON__Number=Sing|PronType=Dem": {"morph": "Number=Sing|PronType=Dem", POS: PRON},
    "PRON__Number=Sing|PronType=Ind": {"morph": "Number=Sing|PronType=Ind", POS: PRON},
    "PRON__Number=Sing|PronType=Int": {"morph": "Number=Sing|PronType=Int", POS: PRON},
    "PRON__Number=Sing|PronType=Rel": {"morph": "Number=Sing|PronType=Rel", POS: PRON},
    "PRON__Person=1|PronType=Prs": {"morph": "Person=1|PronType=Prs", POS: PRON},
    "PRON__Person=3": {"morph": "Person=3", POS: PRON},
    "PRON__Person=3|PrepCase=Pre|PronType=Prs": {"morph": "Person=3|PrepCase=Pre|PronType=Prs", POS: PRON},
    "PRON__Person=3|PronType=Prs": {"morph": "Person=3|PronType=Prs", POS: PRON},
    "PRON__PronType=Ind": {"morph": "PronType=Ind", POS: PRON},
    "PRON__PronType=Int": {"morph": "PronType=Int", POS: PRON},
    "PRON__PronType=Rel": {"morph": "PronType=Rel", POS: PRON},
    "PROPN___": {"morph": "_", POS: PROPN},
    "PUNCT___": {"morph": "_", POS: PUNCT},
    "PUNCT__PunctSide=Fin|PunctType=Brck": {"morph": "PunctSide=Fin|PunctType=Brck", POS: PUNCT},
    "PUNCT__PunctSide=Fin|PunctType=Excl": {"morph": "PunctSide=Fin|PunctType=Excl", POS: PUNCT},
    "PUNCT__PunctSide=Fin|PunctType=Qest": {"morph": "PunctSide=Fin|PunctType=Qest", POS: PUNCT},
    "PUNCT__PunctSide=Ini|PunctType=Brck": {"morph": "PunctSide=Ini|PunctType=Brck", POS: PUNCT},
    "PUNCT__PunctSide=Ini|PunctType=Excl": {"morph": "PunctSide=Ini|PunctType=Excl", POS: PUNCT},
    "PUNCT__PunctSide=Ini|PunctType=Qest": {"morph": "PunctSide=Ini|PunctType=Qest", POS: PUNCT},
    "PUNCT__PunctType=Colo": {"morph": "PunctType=Colo", POS: PUNCT},
    "PUNCT__PunctType=Comm": {"morph": "PunctType=Comm", POS: PUNCT},
    "PUNCT__PunctType=Dash": {"morph": "PunctType=Dash", POS: PUNCT},
    "PUNCT__PunctType=Peri": {"morph": "PunctType=Peri", POS: PUNCT},
    "PUNCT__PunctType=Quot": {"morph": "PunctType=Quot", POS: PUNCT},
    "PUNCT__PunctType=Semi": {"morph": "PunctType=Semi", POS: PUNCT},
    "SCONJ___": {"morph": "_", POS: SCONJ},
    "SYM___": {"morph": "_", POS: SYM},
    "SYM__NumForm=Digit": {"morph": "NumForm=Digit", POS: SYM},
    "SYM__NumForm=Digit|NumType=Frac": {"morph": "NumForm=Digit|NumType=Frac", POS: SYM},
    "VERB__Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part": {"morph": "Gender=Fem|Number=Plur|Tense=Past|VerbForm=Part", POS: VERB},
    "VERB__Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part": {"morph": "Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part", POS: VERB},
    "VERB__Gender=Masc|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin": {"morph": "Gender=Masc|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin", POS: VERB},
    "VERB__Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part": {"morph": "Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part", POS: VERB},
    "VERB__Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part": {"morph": "Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part", POS: VERB},
    "VERB__Mood=Cnd|Number=Plur|Person=1|VerbForm=Fin": {"morph": "Mood=Cnd|Number=Plur|Person=1|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Cnd|Number=Plur|Person=3|VerbForm=Fin": {"morph": "Mood=Cnd|Number=Plur|Person=3|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Cnd|Number=Sing|Person=1|VerbForm=Fin": {"morph": "Mood=Cnd|Number=Sing|Person=1|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Cnd|Number=Sing|Person=2|VerbForm=Fin": {"morph": "Mood=Cnd|Number=Sing|Person=2|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Cnd|Number=Sing|Person=3|VerbForm=Fin": {"morph": "Mood=Cnd|Number=Sing|Person=3|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Imp|Number=Plur|Person=1|VerbForm=Fin": {"morph": "Mood=Imp|Number=Plur|Person=1|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Imp|Number=Plur|Person=2|VerbForm=Fin": {"morph": "Mood=Imp|Number=Plur|Person=2|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Imp|Number=Plur|Person=3|VerbForm=Fin": {"morph": "Mood=Imp|Number=Plur|Person=3|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Imp|Number=Sing|Person=2|VerbForm=Fin": {"morph": "Mood=Imp|Number=Sing|Person=2|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Imp|Number=Sing|Person=3|VerbForm=Fin": {"morph": "Mood=Imp|Number=Sing|Person=3|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Plur|Person=1|Tense=Fut|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=1|Tense=Fut|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Plur|Person=1|Tense=Past|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=1|Tense=Past|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Plur|Person=3|Tense=Past|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=3|Tense=Past|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Sing|Person=1|Tense=Fut|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=1|Tense=Fut|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Sing|Person=1|Tense=Past|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=1|Tense=Past|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Sing|Person=2|Tense=Fut|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=2|Tense=Fut|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Sing|Person=2|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=2|Tense=Imp|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Sing|Person=2|Tense=Past|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=2|Tense=Past|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Ind|Person=3|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Ind|Person=3|Tense=Pres|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Sub|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Sub|Number=Plur|Person=1|Tense=Imp|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Sub|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Sub|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Sub|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Sub|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Sub|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Sub|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Sub|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Sub|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Sub|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Sub|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Sub|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Sub|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Sub|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Sub|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Sub|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin": {"morph": "Mood=Sub|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin", POS: VERB},
    "VERB__Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin": {"morph": "Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin", POS: VERB},
    "VERB__VerbForm=Ger": {"morph": "VerbForm=Ger", POS: VERB},
    "VERB__VerbForm=Inf": {"morph": "VerbForm=Inf", POS: VERB},
    "X___": {"morph": "_", POS: X},
    "_SP": {"morph": "_", POS: SPACE},
}
# fmt: on
