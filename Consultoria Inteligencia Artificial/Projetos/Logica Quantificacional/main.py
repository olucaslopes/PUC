from phrase_parser.knowledge_base import KnowledgeBase
from phrase_parser.sentence_parser import SentenceParser

def main():
    knowledge_base = KnowledgeBase()

    while True:
        # Obtendo input de uma crença
        new_belief = input('Insira uma nova crença ou a palavra \'sair\' para terminar: ')
        if new_belief.lower().strip() == 'sair':
            break

        # Transformando frase do português para expressão do nltk
        parser = SentenceParser(new_belief)
        logic_belief = str(parser.parse())

        print("Expressão lógica: ", logic_belief)

        print("Testando a frase e adicionado na base de crenças...")

        # Faz 4 testes e se sim adiciona na base de crenças
        knowledge_base.add_belief(new_belief, logic_belief)

if __name__ == "__main__":
    main()