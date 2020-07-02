from ...symbols import POS, PUNCT, ADJ, CCONJ, NUM, DET, ADV, ADP, X, VERB
from ...symbols import NOUN, PRON, AUX, SCONJ, INTJ, PART, PROPN


# POS explanations for indonesian available from https://www.aclweb.org/anthology/Y12-1014
TAG_MAP = {
    "NSD": {POS: NOUN},
    "Z--": {POS: PUNCT},
    "VSA": {POS: VERB},
    "CC-": {POS: NUM},
    "R--": {POS: ADP},
    "D--": {POS: ADV},
    "ASP": {POS: ADJ},
    "S--": {POS: SCONJ},
    "VSP": {POS: VERB},
    "H--": {POS: CCONJ},
    "F--": {POS: X},
    "B--": {POS: DET},
    "CO-": {POS: NUM},
    "G--": {POS: ADV},
    "PS3": {POS: PRON},
    "W--": {POS: ADV},
    "O--": {POS: AUX},
    "PP1": {POS: PRON},
    "ASS": {POS: ADJ},
    "PS1": {POS: PRON},
    "APP": {POS: ADJ},
    "CD-": {POS: NUM},
    "VPA": {POS: VERB},
    "VPP": {POS: VERB},
    "X--": {POS: X},
    "CO-+PS3": {POS: NUM},
    "NSD+PS3": {POS: NOUN},
    "ASP+PS3": {POS: ADJ},
    "M--": {POS: AUX},
    "VSA+PS3": {POS: VERB},
    "R--+PS3": {POS: ADP},
    "W--+T--": {POS: ADV},
    "PS2": {POS: PRON},
    "NSD+PS1": {POS: NOUN},
    "PP3": {POS: PRON},
    "VSA+T--": {POS: VERB},
    "D--+T--": {POS: ADV},
    "VSP+PS3": {POS: VERB},
    "F--+PS3": {POS: X},
    "M--+T--": {POS: AUX},
    "F--+T--": {POS: X},
    "PUNCT": {POS: PUNCT},
    "PROPN": {POS: PROPN},
    "I--": {POS: INTJ},
    "S--+PS3": {POS: SCONJ},
    "ASP+T--": {POS: ADJ},
    "CC-+PS3": {POS: NUM},
    "NSD+PS2": {POS: NOUN},
    "B--+T--": {POS: DET},
    "H--+T--": {POS: CCONJ},
    "VSA+PS2": {POS: VERB},
    "NSF": {POS: NOUN},
    "PS1+VSA": {POS: PRON},
    "NPD": {POS: NOUN},
    "PP2": {POS: PRON},
    "VSA+PS1": {POS: VERB},
    "T--": {POS: PART},
    "NSM": {POS: NOUN},
    "NUM": {POS: NUM},
    "ASP+PS2": {POS: ADJ},
    "G--+T--": {POS: PART},
    "D--+PS3": {POS: ADV},
    "R--+PS2": {POS: ADP},
    "NSM+PS3": {POS: NOUN},
    "VSP+T--": {POS: VERB},
    "M--+PS3": {POS: AUX},
    "ASS+PS3": {POS: ADJ},
    "G--+PS3": {POS: PART},
    "F--+PS1": {POS: X},
    "NSD+T--": {POS: NOUN},
    "PP1+T--": {POS: PRON},
    "B--+PS3": {POS: DET},
    "NOUN": {POS: NOUN},
    "NPD+PS3": {POS: NOUN},
    "R--+PS1": {POS: ADP},
    "F--+PS2": {POS: X},
    "CD-+PS3": {POS: NUM},
    "PS1+VSA+T--": {POS: VERB},
    "PS2+VSA": {POS: VERB},
    "VERB": {POS: VERB},
    "CC-+T--": {POS: NUM},
    "NPD+PS2": {POS: NOUN},
    "D--+PS2": {POS: ADV},
    "PP3+T--": {POS: PRON},
    "X": {POS: X},
}
