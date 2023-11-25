from nltk.sem import Expression
from nltk.sem.logic import *


def expressao_para_nltk(frase, sujeito, predicado, negacao=False):
    """TODO Refactor função
    # Pyenchant parece ser uma boa solução para mapear plural para singular
    expressao_para_nltk("Sócrates é homem")
    # Resultado
    homem(socrates)

    expressao_para_nltk("Raul não é cientista.")
    # Resultado
    ¬cientista(raul)

    expressao_para_nltk("Todos os homens são mortais.")
    # Resultado
    all x.(homem(x) -> mortal(x))

    expressao_para_nltk("Todos os homens não são répteis.")
    # Resultado
    ¬exists x.(homem(x) & réptil(x))

    expressao_para_nltk("Algum homem é mortal")
    # Resultado
    exists x.(homem(x) & mortal(x))

    expressao_para_nltk("Algum homem não é palmeirense.")
    # Resultado
    exists x.(homem(x) & ¬palmeirense(x))

    expressao_para_nltk("Nenhum homem é réptil.")
    # Resultado
    ¬exists x.(homem(x) & réptil(x))

    expressao_para_nltk("Nenhum homem não é humano.")
    # Resultado
    ¬exists x.(homem(x) & ¬humano(x))
    """
    if negacao:
        expressao = f"¬{predicado}({sujeito})"
    else:
        expressao = f"{predicado}({sujeito})"
    return Expression.fromstring(expressao)


def separar_expressoes(lista_expressoes):
    premisas = []
    for exp in lista_expressoes:
        partes = exp.split(' ')
        if partes[1] == 'é':
            sujeito = partes[0]
            predicado = partes[2]
            premisas.append((1, sujeito, predicado))
        elif partes[1] == 'não':
            sujeito = partes[0]
            predicado = partes[3]
            premisas.append((2, sujeito, predicado))
        elif partes[0] == 'Todo':
            sujeito = partes[2]
            predicado = partes[4]
            negacao = False if partes[3] == 'é' else True
            premisas.append((3 if not negacao else 4, sujeito, predicado))
        elif partes[0] == 'Algum':
            sujeito = partes[1]
            predicado = partes[3]
            negacao = False if partes[2] == 'é' else True
            premisas.append((5 if not negacao else 6, sujeito, predicado))
        elif partes[0] == 'Nenhum':
            sujeito = partes[1]
            predicado = partes[3]
            negacao = False if partes[2] == 'é' else True
            premisas.append((7 if not negacao else 8, sujeito, predicado))
    return premisas


if __name__ == '__main__':
    # Exemplo de lista de expressões
    expressoes = [
        "Sócrates é homem.",
        "Raul não é cientista.",
        "Todos os homens são mortais.",
        "Todos os homens não são répteis.",
        "Algum homem é mortal.",
        "Algum homem não é palmeirense.",
        "Nenhum homem é réptil.",
        "Nenhum homem não é humano."
    ]

    premisas_separadas = separar_expressoes(expressoes)

    for tipo, sujeito, predicado in premisas_separadas:
        if tipo == 1:
            print(f"{sujeito} é {predicado}")
            exp_nltk = expressao_para_nltk(f"{sujeito} é {predicado}", sujeito, predicado)
        elif tipo == 2:
            print(f"{sujeito} não é {predicado}")
            exp_nltk = expressao_para_nltk(f"{sujeito} não é {predicado}", sujeito, predicado, True)
        elif tipo == 3:
            print(f"Todo {sujeito} é {predicado}")
            exp_nltk = expressao_para_nltk(f"Todo {sujeito} é {predicado}", sujeito, predicado)
        elif tipo == 4:
            print(f"Todo {sujeito} não é {predicado}")
            exp_nltk = expressao_para_nltk(f"Todo {sujeito} não é {predicado}", sujeito, predicado, True)
        elif tipo == 5:
            print(f"Algum {sujeito} é {predicado}")
            exp_nltk = expressao_para_nltk(f"Algum {sujeito} é {predicado}", sujeito, predicado)
        elif tipo == 6:
            print(f"Algum {sujeito} não é {predicado}")
            exp_nltk = expressao_para_nltk(f"Algum {sujeito} não é {predicado}", sujeito, predicado, True)
        elif tipo == 7:
            print(f"Nenhum {sujeito} é {predicado}")
            exp_nltk = expressao_para_nltk(f"Nenhum {sujeito} é {predicado}", sujeito, predicado)
        elif tipo == 8:
            print(f"Nenhum {sujeito} não é {predicado}")
            exp_nltk = expressao_para_nltk(f"Nenhum {sujeito} não é {predicado}", sujeito, predicado, True)

        print("Expressão NLTK correspondente:", exp_nltk)
        print()
