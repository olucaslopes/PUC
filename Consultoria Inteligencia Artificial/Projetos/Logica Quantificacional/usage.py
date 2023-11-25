from phrase_parser.sentence_parser import SentenceParser

parser = SentenceParser("Nenhum homem não é humano.")
result = str(parser.parse())
print(result)
