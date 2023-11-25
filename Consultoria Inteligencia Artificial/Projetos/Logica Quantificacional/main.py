import spacy
from morph import separar_sujeito_predicado
import unicodedata

try:
    nlp = spacy.load('pt_core_news_sm')
except OSError as e:
    raise OSError(('Você precisa baixar o lemmantizador do português.'
                   'Baixe-o com ``$python -m spacy download pt_core_news_sm``'))


# stop_words = set(stopwords.words('portuguese'))


def lemmantize_word(word):
    """
    Lemmantize word, convert to lower and ascii w

    """
    if not isinstance(word, str):
        raise ValueError('word precisa ser um str')
    # Lemmantize
    word = nlp(word)[0].lemma_
    # Lower
    word = word.lower()
    # Remove accents
    word = unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode('utf-8')
    return word


def expressao_para_nltk(frase):
    doc = nlp(frase)
    tokens = [token.lemma_ for token in doc if token.dep_ != 'punct' and token.lemma_]
    # lemma_frase = " ".join(tokens)

    if tokens[0] == 'todo':
        sujeito, predicado = separar_sujeito_predicado(frase)
        lemma_suj, lemma_pred = lemmantize_word(sujeito), lemmantize_word(predicado)
        if any([token == 'não' for token in tokens]):
            # Se é uma frase que contém uma negação em qualquer parte
            # Nega o predicado
            return f'¬exists x.({lemma_suj}(x) & {lemma_pred}(x))'
        else:
            return f'all x.({lemma_suj}(x) -> {lemma_pred}(x))'
    elif tokens[0] == 'algum':
        sujeito, predicado = separar_sujeito_predicado(frase)
        lemma_suj, lemma_pred = lemmantize_word(sujeito), lemmantize_word(predicado)
        if any([token == 'não' for token in tokens]):
            # Se é uma frase que contém uma negação em qualquer parte
            # Nega o predicado
            return f'exists x.({lemma_suj}(x) & ¬{lemma_pred}(x))'
        else:
            return f'exists x.({lemma_suj}(x) & {lemma_pred}(x))'
    elif tokens[0] == 'nenhum':
        sujeito, predicado = separar_sujeito_predicado(frase)
        lemma_suj, lemma_pred = lemmantize_word(sujeito), lemmantize_word(predicado)
        if any([token == 'não' for token in tokens]):
            # Se é uma frase que contém uma negação em qualquer parte
            # Nega o predicado
            return f'¬exists x.({lemma_suj}(x) & ¬{lemma_pred}(x))'
        else:
            return f'¬exists x.({lemma_suj}(x) & {lemma_pred}(x))'
    else:
        sujeito, predicado = separar_sujeito_predicado(frase)
        lemma_suj, lemma_pred = lemmantize_word(sujeito), lemmantize_word(predicado)
        if any([token == 'não' for token in tokens]):
            # Se é uma frase que contém uma negação em qualquer parte
            # Nega o predicado
            return f'¬{lemma_pred}({lemma_suj})'
        else:
            return f'{lemma_pred}({lemma_suj})'

    # return lemma_frase


if __name__ == '__main__':
    phrases = [
        "Sócrates é homem",
        "Raul não é cientista.",
        "Todos os homens são mortais.",
        "Todos os homens não são répteis.",
        "Algum homem é mortal",
        "Algum homem não é palmeirense.",
        "Nenhum homem é réptil.",
        "Nenhum homem não é humano."
    ]
    expecteds = [
        "homem(socrates)",
        "¬cientista(raul)",
        "all x.(homem(x) -> mortal(x))",
        "¬exists x.(homem(x) & reptel(x))",  # Nota: o lemmantizador transforma répteis em reptel
        "exists x.(homem(x) & mortal(x))",
        "exists x.(homem(x) & ¬palmeirense(x))",
        "¬exists x.(homem(x) & reptil(x))",
        "¬exists x.(homem(x) & ¬humano(x))"
    ]

    for phrase, expected in zip(phrases, expecteds):
        output = expressao_para_nltk(phrase)
        print(output == expected)
        print('Phrase:', phrase)
        print('Expected:', expected)
        print('Output:', output)
        print()
