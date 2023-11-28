import pytest
from phrase_parser.knowledge_base import KnowledgeBase
from phrase_parser.sentence_parser import SentenceParser


@pytest.mark.parametrize("p1, p2, p3", [
    ("Sócrates é homem", "Todos os homens são mortais", "Sócrates é mortal"),
    ("Nenhum filósofo fala galês", "Jones é um filósofo", "Jones não fala galês"),
    # ("Todos os lógicos são filósofos.", "Russell é um lógico que não é sábio", "Nem todos os filósofos são sábios.")
])
def test_redundancy(p1, p2, p3):
    p1_logic = SentenceParser(p1).parse()
    p2_logic = SentenceParser(p2).parse()
    p3_logic = SentenceParser(p3).parse()

    belief_base = KnowledgeBase()

    belief_base.add_belief(p1, p1_logic)
    belief_base.add_belief(p2, p2_logic)

    assert belief_base.is_redundant(p3_logic) is True


@pytest.mark.parametrize("p1, p2, p3", [
    ("Sócrates é homem", "Todos os homens são mortais", "Sócrates não é mortal"),
])
def test_inconsistency(p1, p2, p3):
    p1_logic = SentenceParser(p1).parse()
    p2_logic = SentenceParser(p2).parse()
    p3_logic = SentenceParser(p3).parse()

    belief_base = KnowledgeBase()

    belief_base.add_belief(p1, p1_logic)
    belief_base.add_belief(p2, p2_logic)

    assert belief_base.is_inconsistent(p3_logic) is True


@pytest.mark.parametrize('p1', [
    'Todo homem é homem'
])
def test_tautology(p1):
    p1_logic = SentenceParser(p1).parse()

    belief_base = KnowledgeBase()

    assert belief_base.is_tautology(p1_logic) is True


@pytest.mark.parametrize('p1', [
    'Algum homem não é homem'
])
def test_contradiction(p1):
    p1_logic = SentenceParser(p1).parse()

    belief_base = KnowledgeBase()

    assert belief_base.is_contradiction(p1_logic) is True
