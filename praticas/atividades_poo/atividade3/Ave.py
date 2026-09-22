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