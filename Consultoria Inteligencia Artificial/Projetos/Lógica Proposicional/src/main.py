# Escreva uma função python que determina se uma expressão é bem formada ou não
import re


# NÃO FUNCIONA PARA AND OR COM MAIS DE UM CARACTER PQ SPLIT QUEBRA


def split_formula(formula: str) -> tuple:
    """
    Percorre toda a formula até encontrar um conector
    que esteja dentro do primeiro parêntesis e quebra
    a formula em (antes do conector), (conector), (depois do conector).
    Assume que o conector tem 1 character.

    :param formula: str fórmula de lógica proposicional
    :return: tuple (str, str, str) fórmula quebrada em 3 partes tendo como referência o conector principal
    """
    left_i = 0
    brackets_count = 0
    and_or_char = r'&∧|∨'
    for i, e in enumerate(formula):
        if e == '(':
            brackets_count += 1
        elif e == ')':
            brackets_count -= 1
        if brackets_count == 1 and e in and_or_char:
            left_i = i - 1
            break

    left, conector, right = formula[1:left_i + 1], formula[left_i + 1], formula[left_i + 2:-1],
    return left, conector, right


def is_wff(formula: str, print_tree: bool = False, _allow_atomic=False) -> bool:
    """
    :param formula:
    :param print_tree:
    :param _allow_atomic:
    :return:
    """
    not_char = '(~|¬|!)'
    and_or_char = r'(&|∧|\||∨)'

    # Remover espaço em branco
    f = re.sub(r'\s', '', formula)

    #### Verificações básicas ####
    # Deve começar e terminar com parêntesis
    if not re.match(fr'{not_char}?\(.+\)', f) and _allow_atomic is False:
        return False
    # Not vem antes de abre parêntesis e letra e not
    if re.match(f'{not_char}(?![a-zA-Z(¬~!])[^a-zA-Z(¬~!]', f):
        return False
    # And e or está entre letra, abre e fecha parêntesis e not
    if re.findall(fr'(?<![a-zA-Z(¬]){and_or_char}(?![a-zA-Z)¬])', f):
        return False

    if _allow_atomic:
        # Se é uma expressão atômica ela é válida
        match_atomic = re.match(f'{not_char}?[a-zA-Z]', f)
    else:
        match_atomic = False
    # Se começar com not ele é o conectivo principal e deve conter parêntesis
    # Ex.: ¬(P∧¬(¬Q∨R))
    match_not = re.match(rf'{not_char}+(.+)', f)
    if match_atomic:
        if print_tree:
            print(f'{f} é uma wff.')
        return True
    elif match_not:
        # Se o conectivo é valido e a expressão interna é válida
        if re.match(not_char, match_not.groups()[0]) and \
                is_wff(match_not.groups()[1], _allow_atomic=True, print_tree=print_tree):
            if print_tree:
                print(f'{f} é uma wff.')
            return True
    else:
        left, conector, right = split_formula(f)
        if is_wff(left, _allow_atomic=True, print_tree=print_tree) and is_wff(right, _allow_atomic=True,
                                                                              print_tree=print_tree):
            if print_tree:
                print(f'{f} é uma wff.')
            return True
    return False

# Se começar com not o not é um algoritmo principal
# Se encontrar um conectivo e a contagem de parênthesis for igual a um esse é o conectivo principal
# Cada conectivo principal vai ser um nó da árvore
# Cada expressão atômica vai ser uma folha da árvore