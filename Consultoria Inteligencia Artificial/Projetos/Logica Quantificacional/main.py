from phrase_parser.knowledge_base import KnowledgeBase

def main():
    knowledge_base = KnowledgeBase()

    while True:
        phrase = input("Digite uma frase: ")
        print("Frase digitada: ", phrase)

        tautology, contradition, redundant, consistant, logic_phrase = knowledge_base.check_belief(phrase)

        print("Testando a frase...")
        #quando a variavel for True  = Reprovado / False = Aprovado
        if tautology:
            print("Tautologia: Aprovado!")
        else:
            print("Tautologia: Reprovado!")

        if contradition:
            print("Contradição: Aprovado!")
        else:
            print("Contradição: Reprovado!")

        if redundant:
            print("Redundância: Aprovado!")
        else:
            print("Redundância: Reprovado!")

        if consistant:
            print("Consistência: Aprovado!")
        else:
            print("Consistência: Reprovado!")

        if not (tautology or contradition or redundant or consistant):
            print("A frase é válida!")
            print("Adicionando à base de crenças...")
            knowledge_base.add_belief(phrase, logic_phrase)
            print("Base de crenças atualizada: ", knowledge_base.beliefs)
        else:
            print("A frase não é válida!")
            print("Base de crenças atual: ", knowledge_base.beliefs)

        continuar = input("Quer digitar uma nova frase? (S/N): ")
        if continuar.upper() != "S":
            print("Fim!")
            break

if __name__ == "__main__":
    main()