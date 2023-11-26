from phrase_parser.sentence_parser import SentenceParser
from nltk.inference.tableau import TableauProver, Expression


class KnowledgeBase:
    def __init__(self):
        self.beliefs = {}
        self.generated_logic_phrases = False
        self.logic_phrases = list()

    def add_belief(self, phrase, logic_phrase):
        """
        Adds belief to KnowledgeBase if it is valid
        """
        conditions = [self.is_tautology, self.is_contradiction, self.is_redundant, self.is_consistent]
        tautology, contradition, redundant, consistant = [cond(logic_phrase) for cond in conditions]
        if tautology or contradition:
            print("'phrase' não possui conteúdo informacional. Nenhuma informação foi adicionada na base de crenças")
            return None
        elif redundant:
            print('Informação redundante. Nenhuma informação foi adicionada na base de crenças')
        elif consistant:
            print('Informação conflitante com a base de crenças. Nenhuma informação foi adicionada na base de crenças')
            return None
        else:
            self.generated_logic_phrases = False
            self.beliefs[phrase] = logic_phrase
            print(f'Adicionado com sucesso na base de crenças: `{logic_phrase}` ({phrase})')
            return None

    def get_logic_phrases(self):
        self.logic_phrases = [Expression.fromstring(logic) for logic in self.beliefs.values()]
        self.generated_logic_phrases = True
        return self.logic_phrases

    def check_belief(self, phrase):
        logic_phrase = str(SentenceParser(phrase).parse())
        tableau = TableauProver()
        c = Expression.fromstring(logic_phrase)

        tautology = tableau.prove(c, [])
        contradition = tableau.prove(-c, [])
        redundant = tableau.prove(c, [Expression.fromstring(logic) for logic in self.beliefs.values()])
        consistant = tableau.prove(-c, [Expression.fromstring(logic) for logic in self.beliefs.values()])

        return tautology, contradition, redundant, consistant, logic_phrase

    def is_tautology(self, logic_exp, verbose=False):
        """
        Returns True if the expression c is a tautology.

        Args:
            logic_exp: The propositional expression to be tested.
            verbose: Whether show Tableau or not
        Returns:
            True if c is a tautology, False otherwise.
        """

        c = Expression.fromstring(logic_exp)
        return TableauProver().prove(
            goal=c,
            assumptions=[],
            verbose=verbose
        )

    def is_contradiction(self, logic_exp, verbose=False):
        """
        Returns True if the expression c is a contradiction.

        Args:
            logic_exp: The propositional expression to be tested.
            verbose: Whether show Tableau or not

        Returns:
            True if c is a contradiction, False otherwise.
        """

        c = Expression.fromstring(logic_exp)
        return TableauProver().prove(
            goal=-c,
            assumptions=[],
            verbose=verbose
        )

    def is_redundant(self, logic_exp, verbose=False):
        """
        Returns True if the expression c is redundant.

        Args:
            logic_exp: The propositional expression to be tested.
            verbose: Whether show Tableau or not

        Returns:
            True if c is redundant, False otherwise.
        """

        c = Expression.fromstring(logic_exp)
        return TableauProver().prove(
            goal=c,
            assumptions=self.beliefs,
            verbose=verbose
        )

    def is_consistent(self, logic_exp, verbose=False):
        """
        Returns True if the expression c is consistent.

        Args:
            logic_exp: The propositional expression to be tested.
            verbose: Whether show Tableau or not

        Returns:
            True if c is consistent, False otherwise.
        """

        c = Expression.fromstring(logic_exp)
        return TableauProver().prove(
            goal=-c,
            assumptions=self.beliefs,
            verbose=verbose
        )
