from spacy.tokens import Doc
import pytest


# fmt: off
@pytest.mark.parametrize(
    "words,heads,deps,pos,chunk_offsets",
    [
        # un gato -> "un gato"
        (
            ["un", "gato"],
            [1, 1],
            ["det", "ROOT"],
            ["DET", "NOUN"],
            [(0, 2)],
        ),
        # la camisa negra -> "la camisa negra"
        (
            ["la", "camisa", "negra"],
            [1, 1, 1],
            ["det", "ROOT", "amod"],
            ["DET", "NOUN", "ADJ"],
            [(0, 3)],
        ),
        # un lindo gatito -> "un lindo gatito"
        (
            ["Un", "lindo", "gatito"],
            [2, 2, 2],
            ["det", "amod", "ROOT"],
            ["DET", "ADJ", "NOUN"],
            [(0,3)]
        ),
        # una chica hermosa e inteligente -> una chica hermosa e inteligente
        (
            ["Una", "chica", "hermosa", "e", "inteligente"],
            [1, 1, 1, 4, 2],
            ["det", "ROOT", "amod", "cc", "conj"],
            ["DET", "NOUN", "ADJ", "CCONJ", "ADJ"],
            [(0,5)]
        ),
        # Tengo un gato y un perro -> un gato, un perro
        ( 
            ["Tengo", "un", "gato", "y", "un", "perro"],
            [0, 2, 0, 5, 5, 0],
            ["ROOT", "det", "obj", "cc", "det", "conj"],
            ["VERB", "DET", "NOUN", "CCONJ", "DET", "NOUN"],
            [(1,3), (4,6)]
         
        ),
        # Dom Pedro II -> Dom Pedro II
        (
            ["Dom", "Pedro", "II"],
            [0, 0, 0],
            ["ROOT", "flat", "flat"],
            ["PROPN", "PROPN", "PROPN"],
            [(0,3)]
        ),
        # los Estados Unidos -> los Estados Unidos
        (
            ["los", "Estados", "Unidos"],
            [1, 1, 1],
            ["det", "ROOT", "flat"],
            ["DET", "PROPN", "PROPN"],
            [(0,3)]
        ),
        # Miguel de Cervantes -> Miguel de Cervantes
        (
            ["Miguel", "de", "Cervantes"],
            [0, 2, 0],
            ["ROOT", "case", "flat"],
            ["PROPN", "ADP", "PROPN"],
            [(0,3)]
        ),
        (
            ["Rio", "de", "Janeiro"],
            [0, 2, 0],
            ["ROOT", "case", "flat"],
            ["PROPN", "ADP", "PROPN"],
            [(0,3)]
        ),
        # la destrucción de la ciudad -> la destrucción, la ciudad
        (
            ["la", "destrucción", "de", "la", "ciudad"],
            [1, 1, 4, 4, 1],
            ['det', 'ROOT', 'case', 'det', 'nmod'],
            ['DET', 'NOUN', 'ADP', 'DET', 'NOUN'],
            [(0,2), (3,5)]
        ),
        # la traducción de Susana del informe -> la traducción, Susana, informe
        (
            ['la', 'traducción', 'de', 'Susana', 'del', 'informe'],
            [1, 1, 3, 1, 5, 1],
            ['det', 'ROOT', 'case', 'nmod', 'case', 'nmod'],
            ['DET', 'NOUN', 'ADP', 'PROPN', 'ADP', 'NOUN'],
            [(0,2), (3,4), (5,6)]  
       
        ),
        # El gato regordete de Susana y su amigo -> el gato regordete, Susana, su amigo
        (  
            ['El', 'gato', 'regordete', 'de', 'Susana', 'y', 'su', 'amigo'],
            [1, 1, 1, 4, 1, 7, 7, 1],
            ['det', 'ROOT', 'amod', 'case', 'nmod', 'cc', 'det', 'conj'],
            ['DET', 'NOUN', 'ADJ', 'ADP', 'PROPN', 'CCONJ', 'DET', 'NOUN'],
            [(0,3), (4,5), (6,8)]
        ),
        # Afirmó que sigue el criterio europeo y que trata de incentivar el mercado donde no lo hay -> el criterio europeo, el mercado, donde, lo
        (
            ['Afirmó', 'que', 'sigue', 'el', 'criterio', 'europeo', 'y', 'que', 'trata', 'de', 'incentivar', 'el', 'mercado', 'donde', 'no', 'lo', 'hay'],
            [0, 2, 0, 4, 2, 4, 8, 8, 2, 10, 8, 12, 10, 16, 16, 16, 0],
            ['ROOT', 'mark', 'ccomp', 'det', 'obj', 'amod', 'cc', 'mark', 'conj', 'mark', 'xcomp', 'det', 'obj', 'obl', 'advmod', 'obj', 'advcl'],
            ['VERB', 'SCONJ', 'VERB', 'DET', 'NOUN', 'ADJ', 'CCONJ', 'SCONJ', 'VERB', 'ADP', 'VERB', 'DET', 'NOUN', 'PRON', 'ADV', 'PRON', 'AUX'],
            [(3,6), (11,13), (13,14), (15,16)]
        ),
        # Tras indicar que la inversión media en investigación en la Unión Europea se sitúa en el 1,8 por ciento del PIB, frente al 2,8 por ciento en Japón y EEUU, Couceiro dijo que España está en "el buen camino" y se está creando un entorno propicio para la innovación empresarial' -> la inversión media, investigación, la Unión Europea, se, PIB, Japón, EEUU, Couceiro, España, se, un entorno propicio para la innovación empresaria
        (
            ['Tras', 'indicar', 'que', 'la', 'inversión', 'media', 'en', 'investigación', 'en', 'la', 'Unión', 'Europea', 'se', 'sitúa', 'en', 'el', '1,8', 'por', 'ciento', 'del', 'PIB', ',', 'frente', 'al', '2,8', 'por', 'ciento', 'en', 'Japón', 'y', 'EEUU', ',', 'Couceiro', 'dijo', 'que', 'España', 'está', 'en', '"', 'el', 'buen', 'camino', '"', 'y', 'se', 'está', 'creando', 'un', 'entorno', 'propicio', 'para', 'la', 'innovación', 'empresarial'],
            [1, 33, 13, 4, 13, 4, 7, 4, 10, 10, 4, 10, 13, 1, 16, 16, 13, 18, 16, 20, 16, 24, 24, 22, 13, 26, 24, 28, 24, 30, 28, 1, 33, 33, 41, 41, 41, 41, 41, 41, 41, 33, 41, 46, 46, 46, 33, 48, 46, 48, 52, 52, 49, 52],
            ['mark', 'advcl', 'mark', 'det', 'nsubj', 'amod', 'case', 'nmod', 'case', 'det', 'nmod', 'flat', 'obj', 'ccomp', 'case', 'det', 'obj', 'case', 'compound', 'case', 'nmod', 'punct', 'case', 'fixed', 'obl', 'case', 'compound', 'case', 'nmod', 'cc', 'conj', 'punct', 'nsubj', 'ROOT', 'mark', 'nsubj', 'cop', 'case', 'punct', 'det', 'amod', 'ccomp', 'punct', 'cc', 'obj', 'aux', 'conj', 'det', 'nsubj', 'amod', 'case', 'det', 'nmod', 'amod'],
            ['ADP', 'VERB', 'SCONJ', 'DET', 'NOUN', 'ADJ', 'ADP', 'NOUN', 'ADP', 'DET', 'PROPN', 'PROPN', 'PRON', 'VERB', 'ADP', 'DET', 'NUM', 'ADP', 'NUM', 'ADP', 'PROPN', 'PUNCT', 'NOUN', 'ADP', 'NUM', 'ADP', 'NUM', 'ADP', 'PROPN', 'CCONJ', 'PROPN', 'PUNCT', 'PROPN', 'VERB', 'SCONJ', 'PROPN', 'AUX', 'ADP', 'PUNCT', 'DET', 'ADJ', 'NOUN', 'PUNCT', 'CCONJ', 'PRON', 'AUX', 'VERB', 'DET', 'NOUN', 'ADJ', 'ADP', 'DET', 'NOUN', 'ADJ'],
            [(3, 6), (7, 8), (9, 12), (12, 13), (20, 21), (28, 29), (30, 31), (32, 33), (35, 36), (44, 45), (47, 54)]
        ),
    ],
)
# fmt: on
def test_es_noun_chunks(es_vocab, words, heads, deps, pos, chunk_offsets):
    doc = Doc(es_vocab, words=words, heads=heads, deps=deps, pos=pos)
    assert [(c.start, c.end) for c in doc.noun_chunks] == chunk_offsets


def test_noun_chunks_is_parsed_es(es_tokenizer):
    """Test that noun_chunks raises Value Error for 'es' language if Doc is not parsed."""
    doc = es_tokenizer("en Oxford este verano")
    with pytest.raises(ValueError):
        list(doc.noun_chunks)
