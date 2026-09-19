from aulas.programacao_poo.heranca.diretoria.Coordenacao import Coordenacao


class Sala(Coordenacao):
    def __init__(self, laboratorio, tipo, professor, curso, alunos):
        super().__init__(professor, curso, alunos)
        self.__laboratorio = laboratorio
        self.__tipo = tipo

    def ter_aula(self):
        print(f"Aula de {self.cursos} no laboratorio {self.__laboratorio} de {self.__tipo}\n"
              f"Professor: {self.escolher_professor(0)}\n"
              f"Alunos: {self.alunos}\n")

sala_1 = Sala(7,
              "Tecnologia",
              ["João"],
              "Python",
              ["Fulano", "Beltrano", "Ciclano"])

sala_1.ter_aula()