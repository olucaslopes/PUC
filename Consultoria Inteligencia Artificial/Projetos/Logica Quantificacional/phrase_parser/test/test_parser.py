import pytest

from phrase_parser.sentence_parser import SentenceParser


@pytest.mark.parametrize("phrase, expected", [
    ("Sócrates é homem", "homem(socrates)"),
    ("Raul não é cientista.", "-cientista(raul)"),
    ("Todos os homens são mortais.", "all x.(homem(x) -> mortal(x))"),
    ("Todos os homens não são répteis.", "-exists x.(homem(x) & reptel(x))"),
    ("Algum homem é mortal", "exists x.(homem(x) & mortal(x))"),
    ("Algum homem não é palmeirense.", "exists x.(homem(x) & -palmeirense(x))"),
    ("Nenhum homem é réptil.", "-exists x.(homem(x) & reptil(x))"),
    ("Nenhum homem não é humano.", "-exists x.(homem(x) & -humano(x))")
])
def test_sentence_parsing(phrase, expected):
    parser = SentenceParser(phrase)
    result = str(parser.parse())
    assert result == expected
