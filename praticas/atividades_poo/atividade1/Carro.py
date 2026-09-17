class Carro:
    def __init__(self, marca, ano, nome, modelo):
        self.marca = marca
        self.ano = ano
        self.nome = nome
        self.modelo = modelo

    def mostrar(self):
        print(self.marca, self.ano, self.nome, self.modelo)

    def __str__(self):
        return f"Marca: {self.marca}\nAno: {self.ano}\nNome: {self.nome}\nModelo: {self.modelo}"

carro1 = Carro("Volkswagen",
               2013,
               "Golf",
               "Hatch")

carro2 = Carro("Honda",
               2025,
               "Civic",
               "Sedan")

carro3 = Carro("Toyota",
               2020,
               "Hillux SW4",
               "SUV")

carro1.mostrar()