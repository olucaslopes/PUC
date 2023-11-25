"""
Funções para análise morfológica de texto
"""

import spacy

nlp = spacy.load('pt_core_news_sm')


def separar_sujeito_predicado(frase):
    """
    Não é perfeito mais funciona. Frases não podem ter modificadores.

    Exemplo errado: O gato preto dormiu no sofá.
    Essa frase possui o artigo 'o', o adjetivo 'preto' e a locução prepositiva
    'no sofá' que podem modificar as palavras gato e dormiu respectivamente.
    O input correto poderia ser:

    Exemplo de imputs corretos: Gato dormiu
    Exemplo de imputs corretos: Gato é preto

    """
    doc = nlp(frase)
    sujeito = ''
    predicado = ''
    for token in doc:
        if token.dep_ == 'nsubj':
            sujeito += token.text_with_ws
        elif token.dep_ == 'ROOT':
            predicado += token.text + ' '

    sujeito, predicado = sujeito.strip(), predicado.strip()

    if not sujeito or not predicado:
        raise ValueError(f"Não pudemos separar o sujeito e o predicado da '{frase}'. Reformulê-a sem modificadores")
    return sujeito.strip(), predicado.strip()


if __name__ == '__main__':
    # Exemplo de uso
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
    for phrase in phrases:
        sujeito, predicado = separar_sujeito_predicado(phrase)
        print('Frase:', phrase)
        print(f'Sujeito: {sujeito}')
        print(f'Predicado: {predicado}')
        print()
