from phrase_parser.knowledge_base import KnowledgeBase
from phrase_parser.sentence_parser import SentenceParser


def test_socrates_redundancy():
    p1 = 'Sócrates é homem'
    p1_logic = SentenceParser(p1).parse()
    p2 = 'Todos os homens são mortais'
    p2_logic = SentenceParser(p2).parse()
    p3 = 'Sócrates é mortal'
    p3_logic = SentenceParser(p3).parse()

    belief_base = KnowledgeBase()

    belief_base.add_belief(p1, p1_logic)
    belief_base.add_belief(p2, p2_logic)

    assert belief_base.is_redundant(p3_logic) is True
