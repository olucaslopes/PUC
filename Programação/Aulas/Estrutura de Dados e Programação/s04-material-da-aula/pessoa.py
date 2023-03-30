class Pessoa:
    def __init__(self, nome, idade):
        """
        Construtor
        """
        # Atributo nome
        self.__nome = nome #__ (duplo underscore) significa que o atributo é privado

        if (idade < 1 or idade > 120):
            raise ValueError("Não faz sentido essa idade")
        # Atributo idade
        self.__idade = idade #__ (duplo underscore) significa que o atributo é privado

    def get_nome(self):
        """
        Um método getter
        """
        return self.__nome

    def get_idade(self):
        """
        Um método getter
        """
        return self.__idade

    def set_nome(self, val):
        """
        Um método setter
        """
        self.__nome = val

    def set_idade(self, val):
        """
        Um método setter
        """
        self.__idade = val

pes_obj = Pessoa("jeff", -10)
print(pes_obj.get_nome())
