from src import is_wff


def test_no_parenthesis_expression():
    assert is_wff('bla') is False


def test_single_parenthesis_expression():
    assert is_wff('(') is False


def test_expression_without_parenthesis():
    assert is_wff('P & Q') is False


def test_simple_negative_atomic_expression():
    assert is_wff('~(P&Q)') is True


def test_2_conective_negative_expression():
    assert is_wff('¬(P ∧ ¬(¬Q ∨ R))') is True

# print(is_wff('¬(P ∧ ¬(¬Q ∨ R))'), True)
# print(is_wff('((P ∨ (R ∧ ¬S)) ∨∨ ¬(Q ∧ ¬P))'), False)
#
# is_wff('¬(P ∧ ¬(¬Q ∨ R))')
# is_wff('((P ∨ (R ∧ ¬S)) ∨∨ ¬(Q ∧ ¬P))')

# is_wff('¬(P ∧ ¬(¬Q ∨ R))')
# is_wff('((P ∨ (R ∧ ¬S)) ∨∨ ¬(Q ∧ ¬P))')

# print(split_formula('((P ∨ (R ∧ ¬S)) ∨ ¬(Q ∧ ¬P))'.replace(' ', '')))


# print(split_formula('(A∨B)'))


# Not vem antes de abre parêntesis e letra
# And or está entre letra, abre e fecha parêntesis e not


# is_wff('¬(P ∧ ¬(¬Q ∨ R))')
# print(split_formula('(P∧¬(¬Q∨R))'))

# is_wff('((P ∨ (R ∧ ¬S)) ∨ ¬(Q ∧ ¬P))')

# print(is_wff('¬(P ∧ ¬(¬Q ∨ R))', print_tree=True), True)
# print(is_wff('((P ∨ (R ∧ ¬S)) ∨ ¬(Q ∧ ¬P))'), True)
# print(is_wff('¬(P ∧ ¬(¬Q ∨ R))'), True)
# print(is_wff('((P ∨ (R ∧ ¬S)) ∨ ¬(Q ∧ ¬P))'), True)
# print(is_wff('(((((R ∧ S) ∨ ¬P) ∨ ¬¬Q) ∨ ¬(S ∧ (¬Q ∨ R))) ∧ ¬(P ∧ ¬(¬Q ∨R)))'), True)