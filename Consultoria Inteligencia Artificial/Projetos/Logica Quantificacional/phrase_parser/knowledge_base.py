from phrase_parser.sentence_parser import SentenceParser
from nltk.sem.logic import *
from nltk.inference.tableau import *

class KnowledgeBase:
    def __init__(self):
        self.base_crencas = {}

    def add_belief(self, phrase, logic_phrase):
        self.base_crencas[phrase] = logic_phrase

    def check_belief(self, phrase):
        logic_phrase = str(SentenceParser(phrase).parse())
        tableau = TableauProver()
        c = Expression.fromstring(logic_phrase)

        tautology = tableau.prove(c, [])
        contradition = tableau.prove(-c, [])
        redundant = tableau.prove(c, [Expression.fromstring(logic) for logic in self.base_crencas.values()])
        consistant = tableau.prove(-c, [Expression.fromstring(logic) for logic in self.base_crencas.values()])

        return tautology, contradition, redundant, consistant, logic_phrase