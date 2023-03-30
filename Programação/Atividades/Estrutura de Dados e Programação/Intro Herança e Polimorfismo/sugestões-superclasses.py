import random
#*******************************************************************************
# SUPER CLASSE
#*******************************************************************************
class Eletrodomestico:
    """
    Essa classe engloba todos os eletrodomésticos definidos
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
        
class HomeTheater(Eletrodomestico):
    """
    """

    def __init__(self):
        """
        Inicializador
        """
        super().__init__()
        self.volume = 0

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



class Televisão(Eletrodomestico):
    """
    Esta classe representa aparelhos de televisão
    """
    def __init__(self):
        """
        Inicializador
        """
        super().__init__()
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


class Microondas(Eletrodomestico):
    """
    """

    def __init__(self):
        """
        Inicializador
        """
        super().__init__()

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

mc = Microondas()
mc.aquecer(30)






#*******************************************************************************
# SUPER CLASSE
#*******************************************************************************

class Pessoa:
    
    def __init__(self, nome, sexo):
        if sexo not in ['M','F','f','m']:
            raise ValueError(
                "Sexo precisa ser uma string com valor 'M' ou 'F'.")
        elif not isinstance(nome, str):
            raise ValueError("Nome precisa ser uma string.")
        self.nome = nome
        self.sexo = sexo.upper()
        
    def reclamar():
        if random.random() < 0.5:
            print("Meu salário tá muito baixo!")
        else:
            print("Eu trabalho muito!")

class Cientista(Pessoa):
    """
    """
    def __init__(self, nome, sexo, rf, nivel_acesso):
        """
        Inicializador
        Args:
            rf: registro funcional
            nome: nome da funcionaria
            nivel_acesso: nivel de acesso
        """
        super().__init__(nome, sexo)
        self.rf = rf
        self.nivel_acesso = nivel_acesso

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
func = Cientista("Paula Silva", "F", "RF-123456", 10)
func.entrar_no_lab_1()


class Professora(Pessoa):
    """
    """
    def __init__(self, nome, rf):
        """
        Inicializador
        Args:
            rf: registro funcional
        """
        sexo = "F"
        super().__init__(nome, sexo)
        self.rf = rf

    def ver_holerite(self, mes, ano):
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
profa = Professora("Heloisa", "RF-123456")
profa.ver_holerite(9, 2021)


class Medica(Pessoa):
    """
    """

    def __init__(self, nome, crm, uf, especialidade):
        """
        Inicializador
        Args:
            crm: CRM do médico
            uf: UF do CRM
            nome: nome do médico
            especialidade: especialidade do médico
        """
        sexo = 'f'
        super().__init__(nome, sexo)
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
med = Medica("Heloísa", 123456, 'ES', 'Pneumologista')
receita = "Respirar ar puro 24 horas por dia"
med.receitar(receita, "Jefferson O. Silva", "104.345.978-02")


class Estudante(Pessoa):
    """
    """

    def __init__(self, nome, sexo, ra):
        """
        Inicializador
        Args:
            ra: registro do aluno
            nome: nome do estudante
        """
        super().__init__(nome, sexo)
        self.ra = ra

    def ver_historico(self):
        """
        Mostra o histórico do aluno
        """
        print("Este é seu histórico escolar")

# Exemplo de uso
estudante = Estudante("Fulano de Tal", "f", "RA19003465")
estudante.ver_historico()