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
    def idade(self, nova_idade):
        if nova_idade > 0:
            self.__idade = nova_idade
        else:
            print("Erro: Idade inválida")

    @property
    def nivel_fome(self):
        return self.__nivel_fome

    @nivel_fome.setter
    def nivel_fome(self, novo_nivel):
        self.__nivel_fome = novo_nivel
        if novo_nivel < 0:
            novo_nivel = 0
            self.__nivel_fome = novo_nivel
            print("intervalo de 0 a 100")
        elif novo_nivel > 100:
            novo_nivel = 100
            self.__nivel_fome = novo_nivel
            print(f"intervalo de 0 a 100")
        else:
            self.__nivel_fome = novo_nivel


    def alimentar(self, porcao):
        if porcao >= self.__nivel_fome:
            self.__nivel_fome = 0
            print(f"A fome foi matada com {porcao}: {self.__nivel_fome}")
        elif 0 < porcao < self.__nivel_fome:
            fome_reduzida = self.__nivel_fome - porcao
            self.__nivel_fome = fome_reduzida
            print(f"Nivel de fome atualizada: {self.__nivel_fome}")
        else:
            print("Erro: Porção inválida")

    def emitir_som(self):
        print(f"O {self.__nome} faz um som genêrico")

    def exibir_resumo(self):
        return print(f"Nome: {self.__nome}\n"
                f"Idade: {self.__idade}\n"
                f"Nivel de Fome: {self.__nivel_fome}")