import spacy
import unicodedata

from parser.layers.existential_quantification_layer import ExistentialQuantificationLayer
from parser.layers.simple_statement_layer import SimpleStatementLayer
from parser.layers.universal_negation_layer import UniversalNegationLayer
from parser.layers.universal_quantification_layer import UniversalQuantificationLayer


class SentenceParser:
    def __init__(self, sentence):
        self.sentence = sentence
        self.nlp = spacy.load('pt_core_news_sm')
        self.doc = self.nlp(sentence)
        self.tokens = self.convert_to_tokens(self.doc)
        self.layers = [
            UniversalQuantificationLayer,
            ExistentialQuantificationLayer,
            UniversalNegationLayer,
            SimpleStatementLayer
        ]

    @staticmethod
    def _remove_accents(word):
        return (
            unicodedata.normalize('NFD', word)
            .encode('ascii', 'ignore')
            .decode('utf-8')
        )

    def lemmatize_word(self, word):
        word = self.nlp(word)[0].lemma_
        word = word.lower()
        return self._remove_accents(word)

    def convert_to_tokens(self, sentence):
        return [token.lemma_ for token in self.nlp(sentence) if token.dep_ != 'punct' and token.lemma_]

    def separate_subject_predicate(self, sentence):
        if not isinstance(sentence, str):
            raise ValueError("Input must be a string.")

        doc = self.nlp(sentence)
        subject_parts = []
        predicate_parts = []

        for token in doc:
            if token.dep_ == 'nsubj':
                subject_parts.append(token.text_with_ws)
            elif token.dep_ == 'ROOT':
                predicate_parts.append(token.text)

        subject = ' '.join(subject_parts).strip()
        predicate = ' '.join(predicate_parts).strip()

        if not subject or not predicate:
            raise ValueError(
                f"Could not separate subject and predicate from '{sentence}'. Try a sentence without modifiers.")

        return subject, predicate

    def parse(self):
        result = self.sentence
        for Layer in self.layers:
            layer_instance = Layer(self)
            result = layer_instance.apply_rule()
            self.sentence = result
        return result
