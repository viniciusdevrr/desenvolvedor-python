from Animal import Animal

class Ave(Animal):
    def __init__(self, nome, idade, nivel_fome, envergadura_asas):
        super().__init__(nome, idade, nivel_fome)
        self.__envergadura_asas = envergadura_asas

    @property
    def envergadura_asas(self):
        return self.__envergadura_asas

    @envergadura_asas.setter
    def envergadura_asas(self, envergadura_asas):
        self.__envergadura_asas = envergadura_asas

    def voar(self):
        if self.nivel_fome <= 80:
            print(f"{self.nome} voou com suas asas de {self.envergadura_asas} cm!")
            self.nivel_fome += 15
        else:
            print(f"{self.nome} está faminto demais para voar!")

    def emitir_som(self):
        print(f"{self.nome} canta um som melodioso!")

    def exibir_resumo(self):
        super().exibir_resumo()
        print(f"Envergadura das asas: {self.__envergadura_asas}")