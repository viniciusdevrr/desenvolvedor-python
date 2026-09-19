class Coordenacao:
    def __init__(self, professor, curso, alunos ):
        self.__professor = professor
        self.__curso = curso
        self.__alunos = alunos

    @property
    def cursos(self):
        return self.__curso

    @property
    def professor(self):
        return self.__professor

    @property
    def alunos(self):
        return self.__alunos

    def escolher_professor(self, index_professor):
        index_professor = ["Joao", "Max"]
        return self.__professor[index_professor]