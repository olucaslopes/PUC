import unittest

from parser.sentence_parser import SentenceParser


class TestSentenceParser(unittest.TestCase):

    def test_sentence_parsing(self):
        phrases = [
            "Sócrates é homem",
            "Raul não é cientista.",
            "Todos os homens são mortais.",
            "Todos os homens não são répteis.",
            "Algum homem é mortal",
            "Algum homem não é palmeirense.",
            "Nenhum homem é réptil.",
            "Nenhum homem não é humano."
        ]
        expected = [
            "homem(socrates)",
            "¬cientista(raul)",
            "all x.(homem(x) -> mortal(x))",
            "¬exists x.(homem(x) & reptel(x))",
            "exists x.(homem(x) & mortal(x))",
            "exists x.(homem(x) & ¬palmeirense(x))",
            "¬exists x.(homem(x) & reptil(x))",
            "¬exists x.(homem(x) & ¬humano(x))"
        ]

        for phrase, expected in zip(phrases, expected):
            with self.subTest(phrase=phrase):
                parser = SentenceParser(phrase)
                result = str(parser.parse())
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
