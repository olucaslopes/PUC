from phrase_parser.layers.abstract_layer import Layer


class UniversalQuantificationLayer(Layer):
    def __init__(self, parser):
        super().__init__(parser)

    def apply_rule(self):
        if self.first_token == 'todo':
            lemma_suj, lemma_pred = self.separate_subject_predicate_and_lemmatize()
            if self.is_negation:
                return f'-exists x.({lemma_suj}(x) & {lemma_pred}(x))'
            else:
                return f'all x.({lemma_suj}(x) -> {lemma_pred}(x))'
        return self.sentence
