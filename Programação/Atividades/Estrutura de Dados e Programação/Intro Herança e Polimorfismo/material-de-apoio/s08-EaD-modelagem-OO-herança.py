# Definição da classe
class Visitante:
 def __init__(self, cpf, nome):
        """
        Inicializador
        Args:
        cpf: identificação única do visitante
        nome: nome do visitante
        """
        self.cpf = cpf
        self.nome = nome

# Exemplo de uso
visitante = Visitante(0, "Doctor Who")
#print(visitante.nome)

#*******************************************************************************
# NOVA CLASSE
#*******************************************************************************

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
#print(cifradorP.cifrar("João gosta de comer feijão e farinha."))

"""
A partir dos exemplos acima, fazer a modelagem OO das classes a seguir. REFLITA sobre os atributos e os métodos que cada classe deve ter. Considere somente aquilo que é mais essencial nas classes (você é livre para julgar). NÃO UTILIZE RECURSOS NÃO VISTOS EM AULA COMO DECORATORS E PROPERTIES porque estão fora dos objetivo de aprendizagem deste momento. Não é necessário criar uma implementação para os métodos. Utilize prints e a palavra-chave pass para representar a implementação. É fundamental documentar os métodos. Ofereça uma descrição sucinta para o propósito do método e cada parâmetro. Não é necessário utilizar getters e setters.
"""

#*******************************************************************************
# NOVA CLASSE
#*******************************************************************************

class Televisão:
    """
    Esta classe representa aparelhos de televisão
    """
    def __init__(self):
        """
        Inicializador
        """
        self.ultimo_canal = 0
        self.canal_atual = 0
        self.volume = 0

    def próximo_canal(self):
        """
        Vai para o próximo canal
        """
        self.canal_anterior = self.canal_atual
        self.canal_atual += 1

    def canal_anterior(self):
        """
        Vai para o canal anterior
        """
        self.canal_anterior = self.canal_atual
        self.canal_atual -= 1

    def aumentar_volume(self):
        """
        Aumenta o volume do aparelho
        """
        self.volume += 1

    def diminuir_volume(self):
        """
        Diminui o volume do aparelho
        """
        self.volume -= 1

    def retornar_ao_último_canal(self):
        """
        Retorna ao último canal
        """
        self.canal_atual = self.canal_anterior

    def ir_para_canal(self, canal):
        """
        Vai para o canal especificado em canal
        Args:
            canal: o canal para qual a TV deve mudar
        """
        self.canal_anterior = self.canal_atual
        self.canal_atual = canal

# Exemplo de uso

tv1 = Televisão()
tv1.próximo_canal()
tv1.ir_para_canal(10)
tv1.retornar_ao_último_canal()
#print(f"canal atual: {tv.canal_atual}")

tv2 = Televisão()
tv2.ir_para_canal(20)

#*******************************************************************************
# NOVA CLASSE
#*******************************************************************************

class HomeTheater:
    """
    """

    def __init__(self):
        """
        Inicializador
        """
        self.estado = True
        self.volume = 0

    def ligar_desligar(self):
        """
        Liga e desliga o aparelho
        """
        self.estado = not self.estado

    def aumentar_volume(self):
        """
        Aumenta o volume do aparelho
        """
        self.volume += 1

    def diminuir_volume(self):
        """
        Diminui o volume do aparelho
        """
        self.volume -= 1

# Exemplo de uso

ht = HomeTheater()
ht.aumentar_volume()
print(ht.volume)
print(ht.estado)

#*******************************************************************************
# NOVA CLASSE
#*******************************************************************************

class Microondas:
    """
    """

    def __init__(self):
        """
        Inicializador
        """
        # estado = Quando o objeto é criado, por padrão, o aparelho é inicializado ligado
        self.estado = True

    def ligar_desligar(self):
        """
        Liga e desliga o aparelho
        """
        self.estado = not self.estado

    def aquecer(self, tempo):
        """
        Aquece o aparelho
        Args:
            tempo: O tempo em segundos que o aparelho irá funcionar
        """
        if (self.estado):
            print(f"Aquece o alimento por {tempo}")
        else:
            print("Ligue o aparelho")

# Exemplo de uso

mc = Microondas(10, 8)
print(mc.aquecer(30))

#*******************************************************************************
# NOVA CLASSE
#*******************************************************************************

class TelaMonitor:
    """
    """

    def __init__(self):
        """
        Inicializador
        """
        # estado = Quando o objeto é criado, por padrão, o aparelho é inicializado ligado
        self.estado = True

        # briho: nível de brilho da inicialização
        self.brilho = 30

        # lim_sup_brilho: limite superior do brilho do monitor
        self.lim_sup_brilho = 100

        # lim_inf_brilho: limite inferior do brilho do monitor
        self.lim_inf_brilho = 0

    def ligar_desligar(self):
        """
        Liga e desliga o aparelho
        """
        self.estado = not self.estado

    def aumentar_brilho(self):
        """
        Aumenta o brilho do monitor até o limite superior
        """
        if (self.brilho < self.lim_sup_brilho):
            self.brilho += 1

    def diminuir_brilho(self):
        """
        Diminui o brilho do monitor até o limite inferior
        """
        if (self.brilho < self.lim_inf_brilho):
            self.brilho -= 1

# Exemplo de uso
tm = TelaMonitor()
tm.aumentar_brilho()
print(f"Brilho atual do monitor: {tm.brilho}")

#*******************************************************************************
# NOVA CLASSE
#*******************************************************************************

class Elevador:
    """
    """

    def __init__(self):
        # Um elevador sempre inicia no térreo por padrão
        self.andar_atual = 0

        # Andar mais alto do prédio
        self.topo = 27

        # Andar mais baixo do prédio
        self.ult_subsolo = -2

    def ir_para_andar(self, andar):
        """
        Instrui o elevador a mudar de andar
        Args:
            andar: o número do andar para o qual se deseja ir
        """
        if (andar <= self.topo and andar >= self.ult_subsolo):
            print(f"Indo para o andar {andar}")
            self.andar_atual = andar
        else:
            print(f"Andar deve estar entre {self.ult_subsolo} e {self.topo}")

# Exemplo de uso
elevador = Elevador()
elevador.ir_para_andar(17)


#*******************************************************************************
# NOVA CLASSE
#*******************************************************************************

class ConversorDeTemp:
    """
    """

    def kelvin_para_celsius(self,temp):
        """
        Converte temp em kelvin para celsius
        """
        return temp - 273

    def kelvin_para_fahrenheit(self,temp):
        """
        Converte temp em kelvin para fahrenheit
        """
        return (temp - 273) * 1.8 + 32

    def celsius_para_kelvin(self,temp):
        """
        Converte temp em celsius para kelvin
        """
        return temp + 273

    def celsius_para_fahrenheit(self,temp):
        """
        Converte temp em celsius para fahrenheint
        """
        return temp * 1.8 + 32

    def fahrenheit_para_celsius(self,temp):
        """
        Converte temp em fahrenheit para celsius
        """
        return (temp - 32) * (5/9)

    def fahrenheit_para_kelvin(self, temp):
        """
        Converte temp em fahrenheit para kelvin
        """
        return ((temp - 32) * (5/9)) + 273.15

# Exemplo de uso
conv_temp = ConversorDeTemp()
temp = 45
print(f"{temp} graus Celsius equivalem a {conv_temp.celsius_para_kelvin(temp)} em Kelvin")


#*******************************************************************************
# NOVA CLASSE
#*******************************************************************************

class Heroi:
    """
    """
    def usar_visao_de_raio_X(self):
        """
        Aciona a visão de raio X
        """
        print("usando a visão de raio X")

    def voar(self):
        """
        Inicia voo
        """
        print("voando")

# Exemplo de uso
heroi = Heroi()
heroi.voar()

#*******************************************************************************
# NOVA CLASSE
#*******************************************************************************

class Funcionaria:
    """
    """
    def __init__(self, rf, nome, nivel_acesso):
        """
        Inicializador
        Args:
            rf: registro funcional
            nome: nome da funcionaria
            nivel_acesso: nivel de acesso
        """
        self.rf = rf
        self.nome = nome
        self.nivel_acesso = nivel_acesso
        # Não se sabe a razão, mas essa classe só serve para mulheres. Por isso, o sexo é fixo
        self.sexo = "F"

    def entrar_no_lab_1(self):
        """
        Método de liberação de entrada no laboratório
        """
        NIVEL_ACESSO_LAB = 15
        if (self.nivel_acesso >= NIVEL_ACESSO_LAB):
            print("Laboratório 1 liberado")
        else:
            print(f"Somente funcionários com acesso nível {NIVEL_ACESSO_LAB} podem entrar no laboratório")

# Exemplo de uso
func = Funcionaria("RF-123456", "Paula Silva", 10)
func.entrar_no_lab_1()

#*******************************************************************************
# NOVA CLASSE
#*******************************************************************************

class Professora:
    """
    """
    def __init__(self, rf):
        """
        Inicializador
        Args:
            rf: registro funcional
        """
        self.rf = rf
        self.sexo = "F"

    def ver_holerite(mes, ano):
        """
        Mostra as informações de pagamento
        Args:
            mes: mes do holerite desejado
            ano: ano do holerite desejado
        """
        MES_INICIO = 1 # busca as informações reais no BD
        ANO_INICIO = 1999 # busca as informações reais no BD
        if (ano > ANO_INICIO):
            print("Este é seu holerite")
        elif (ano == ANO_INICIO):
            if (mes >= MES_INICIO):
                print("Este é seu holerite")
            else:
                print("Holerite antes da sua contratação")
        else:
            print("Holerite antes da sua contratação")

# Exemplo de uso
profa = Professora("RF-123456")
profa.ver_holerite(9, 2021)

#*******************************************************************************
# NOVA CLASSE
#*******************************************************************************

class Medica:
    """
    """

    def __init__(self, crm, uf, nome, especialidade):
        """
        Inicializador
        Args:
            crm: CRM do médico
            uf: UF do CRM
            nome: nome do médico
            especialidade: especialidade do médico
        """
        self.crm = crm
        self.uf = uf
        self.nome = nome
        self.especialidade = especialidade
        self.sexo = "F"

    def receitar(self, receita, nome_paciente, cpf=None):
        """
        Prescreve medicamento para um paciente
        Args:
            nome_paciente: nome do paciente
            cpf: cpf do paciente (padrão None)
        """
        if (cpf == None):
            cpf = "Sem CPF"
        print(f"Nome: {nome_paciente}\nCPF: {cpf}\n\n{receita}\n\n{self.nome}\n{self.crm}/{self.uf}\n{self.especialidade}")

# Exemplo de uso
med = Medica(123456, 'ES', 'Margareth Dalcolmo', 'Pneumologista')
receita = "Respirar ar puro 24 horas por dia"
med.receitar(receita, "Jefferson O. Silva", 104.345.978-02)

#*******************************************************************************
# NOVA CLASSE
#*******************************************************************************

class Estudante:
    """
    """

    def __init__(self, ra, nome):
        """
        Inicializador
        Args:
            ra: registro do aluno
            nome: nome do estudante
        """
        self.ra = ra
        self.nome = nome

    def ver_historico(self):
        """
        Mostra o histórico do aluno
        """
        print("Este é seu histórico escolar")

# Exemplo de uso
estudante = Estudante("RA19003465", "Fulano de Tal")
estudante.ver_historico()


#*******************************************************************************
# NOVA CLASSE
#*******************************************************************************

class Termometro:
    def __init__(self):
        """
        Inicializador
        """
        # Armazena a última temperatura do termômetro
        self.temperatura = 0

    def aferir(self):
        """
        Afere a temperatura
        """
        # lógica que calcula de vdd a temperatura
        self.temperatura = 39.5
        return self.temperatura

# Exemplo de uso
term = Termometro()
print(f"Afere a temperatura: {term.aferir()}")

#*******************************************************************************
# NOVA CLASSE
#*******************************************************************************

class Fogao:
    """
    Na essência, um Fogão pode ser idêntico a um Microondas, embora possa ter
    métodos adicionais
    """
    def __init__(self):
        """
        Inicializador
        """
        # estado = Quando o objeto é criado, por padrão, o aparelho é inicializado ligado
        self.estado = True

    def ligar_desligar(self):
        """
        Liga e desliga o aparelho
        """
        self.estado = not self.estado

    def aquecer(self, tempo):
        """
        Aquece o aparelho
        Args:
            tempo: O tempo em segundos que o aparelho irá funcionar
        """
        if (self.estado):
            print(f"Aquece o alimento por {tempo}")
        else:
            print("Ligue o aparelho")

    def acender_boca(self, n_boca):
        """
        Acende uma boca do fogão
        """
        print(f"Acendi a boca {n_boca}")

# Exemplo de uso
fogao = Fogao()
fogao.acender_boca(3)

#*******************************************************************************
# NOVA CLASSE
#*******************************************************************************

class Carro:
    def __init__(self):
        """
        Inicializador
        """
        # estado = Quando o objeto é criado, por padrão, o aparelho é inicializado ligado
        self.estado = True
        self.velocidade = 0
        # Seria uma boa ideia limitar a velocidade a uma máxima

    def ligar_desligar(self):
        """
        Liga e desliga o aparelho
        """
        self.estado = not self.estado

    def acelerar(self):
        """
        Acelera o carro em um ponto
        """
        if (self.estado):
            self.velocidade += 1

    def frear(self):
        """
        Acelera o carro em um ponto
        """
        if (self.estado):
            self.velocidade -= 1

# Exemplo de uso
carro = Carro()
carro.acelerar()
print(f"A velocidade do carro é {carro.velocidade}")

#*******************************************************************************
# NOVA CLASSE
#*******************************************************************************

class Impressora:
    """
    """
    def __init__(self):
        """
        Inicializador
        """
        self.nivel_cartucho = 100

    def trocar_cartucho(self):
        """
        Atualiza o nível de tinta para o cartucho
        """
        self.nivel_cartucho = 100

    def imprimir(self, texto):
        """
        Imprime o texto na impressora
        Args:
            texto: O texto a ser impresso na impressora
        """
        if (self.nivel_cartucho > 0):
            print(f"Texto impresso na impressora:\n\n{texto}")
            self.nivel_cartucho -= 1
        else:
            print("Troque o cartucho da impressora")

# Exemplo de uso
imp = Impressora()
imp.imprimir("Este é meu documento")
print(f"Nível de tinta da impressora {imp.nivel_cartucho}")
