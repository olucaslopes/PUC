# Definição da classe
class Visitante:
 def __init__(self, cpf, nome):
        """
        Construtor
        Args:
        cpf: identificação única do visitante
        nome: nome do visitante
        """
        self.cpf = cpf
        self.nome = nome

# Exemplo de uso
visitante = Visitante(0, "Doctor Who")
print(visitante.nome)

# Definição da classe
class CifradorLinguaDoPê:
    def cifrar(self, mensagem_ptbr):
        """
        Cifra uma mensagem em pt-BR para a língua do Pê
        Args:
        mensagem_ptbr: mensagem em português
        """
        # Faz a cifra da mensagem (não precisa implementar)
        return "PÊJoPÊão PÊgosPÊta PÊde PÊcoPÊmer PÊfeiPÊjão PÊe PÊfaPÊriPÊnha."

# Exemplo de uso
cifradorP = CifradorLinguaDoPê()
print(cifradorP.cifrar("João gosta de comer feijão e farinha."))

"""
A partir dos exemplos acima, fazer a modelagem OO das classes a seguir. REFLITA sobre os atributos e os métodos que cada classe deve ter. Considere somente aquilo que é mais essencial nas classes (você é livre para julgar). NÃO UTILIZE RECURSOS NÃO VISTOS EM AULA COMO DECORATORS E PROPERTIES porque estão fora dos objetivo de aprendizagem deste momento. Não é necessário criar uma implementação para os métodos. Utilize prints e a palavra-chave pass para representar a implementação. É fundamental documentar os métodos. Ofereça uma descrição sucinta para o propósito do método e cada parâmetro. Não é necessário utilizar getters e setters.
"""

class Televisão:
    def __init__(self, status = "Ligada", canal=0):
        """
        Construtor
        Args:
        status: se a tv está ligada ou desligada
        canal: canal atual da tv
        """
        self._status = status
        self._canal = canal

    def avançar_canal(self):
        """
        Avança um int no canal
        """
        self._canal += 1

    def retroceder_canal(self):
        """
        Retrocede um int no canal
        """
        self._canal -= 1


class HomeTheater:
    pass

class Microondas:
    pass

class TelaMonitor:
    pass

class Elevador:
    pass

class ConversorDeTemp:
    pass

class Herói:
    pass

class Funcionária:
    pass

class Professora:
    pass

class Médica:
    pass

class Estudante:
    def __init__(self, nome, turma):
        self.nome = nome
        self.turma = turma
    def pegar_nome(self):
        return self.nome
    def pegar_turma(self):
        return self.turma

class Termômetro:
    pass

class Fogão:
    pass

class Carro:
    def __init__(self, cor="Preto", limpo=False)
        self.cor = cor
        self.limpo = limpo
    def limpar_carro(self):
        self.limpo = True
        print("O carro agora está limpo!")
    def pintar_carro(self, nova_cor):
        self.cor = nova_cor
        print("O carro agora tem uma nova pintura!")

class Impressora:
    pass

class Celular:
    pass

class FoneDeOuvido:
    pass

class RelógioEsperto:
    pass

class MarcaPasso:
    pass

class AferidorDePressãoArterial:
    pass

class ControleRemotoDePortão:
    pass

class TelefoneAnalógico:
    pass

class PianoElétrico:
    pass

class Temperatura:
    pass

class TabelaDePreçoDeCarros:
    pass

class Produto:
    pass

class PesoDeBagagem:
    pass

class Balança:
    pass

class CadeiraDeMassagem:
    pass
