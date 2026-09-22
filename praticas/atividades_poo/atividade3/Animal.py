class Animal:
    def __init__(self, nome, idade, nivel_fome):
        self.__nome = nome
        self.__idade = idade
        self.__nivel_fome = nivel_fome

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade
        if idade > 0:
            self.__idade = idade
            print(f"A idade do {self.__nome} foi a atualizada para {self.__idade}.")
        else:
            print("Erro: Idade inválida")

    @property
    def nivel_fome(self):
        return self.__nivel_fome

    @nivel_fome.setter
    def nivel_fome(self, nivel_fome):
        self.__nivel_fome = nivel_fome
        if nivel_fome < 0:
            nivel_fome = 0
            self.__nivel_fome = nivel_fome
            print("intervalo de 0 a 100")
        elif nivel_fome > 100:
            nivel_fome = 100
            self.__nivel_fome = nivel_fome
            print(f"intervalo de 0 a 100")
        else:
            self.__nivel_fome = nivel_fome
            print(f"Nivel de Fome atualizado: {self.__nivel_fome}")


    def alimentar(self, porcao):
        if porcao > 0:
            fome_reduzida = self.__nivel_fome - porcao
            print(f"Fome reduzida para: {fome_reduzida}")
        else:
            print("Erro: Porção inválida")

    def emitir_som(self):
        print(f"O {self.__nome} faz um som genêrico")

    def exibir_resumo(self):
        return print(f"METODO: EXIBIR_RESUMO\n"
                f"Nome: {self.__nome}\n"
                f"Idade: R$ {self.__idade}\n"
                f"Nivel de Fome: {self.__nivel_fome}\n")