from abc import ABC, abstractmethod


class Layer(ABC):
    def __init__(self, parser):
        self.parser = parser
        self.tokens = self.parser.tokens
        self.first_token = self.tokens[0] if self.tokens else None
        self.sentence = self.parser.sentence

    def separate_subject_predicate_and_lemmatize(self):
        subject, predicate = self.parser.separate_subject_predicate(self.sentence)
        lemma_suj = self.parser.lemmantize_word(subject)
        lemma_pred = self.parser.lemmantize_word(predicate)
        return lemma_suj, lemma_pred

    @property
    def is_negation(self) -> bool:
        return any(token == 'não' for token in self.tokens)

    @abstractmethod
    def apply_rule(self) -> str:
        pass
