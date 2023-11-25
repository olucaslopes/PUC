from phrase_parser.layers.abstract_layer import Layer


class SimpleStatementLayer(Layer):
    def __init__(self, parser):
        super().__init__(parser)

    def apply_rule(self):
        if self.first_token != 'todo' and self.first_token != 'algum' and self.first_token != 'nenhum':
            lemma_suj, lemma_pred = self.separate_subject_predicate_and_lemmatize()
            if self.is_negation:
                return f'¬{lemma_pred}({lemma_suj})'
            else:
                return f'{lemma_pred}({lemma_suj})'
        return self.sentence
