class Carro:
    def __init__(self, marca, ano, nome, modelo, cor):
        self.marca = marca
        self.ano = ano
        self.nome = nome
        self.modelo = modelo
        self.cor = cor

    def __str__(self):
        return (f"Informações do Veiculo:\n\t"
                f"Marca: {self.marca}\n\t"
                f"Ano: {self.ano}\n\t"
                f"Nome: {self.nome}\n\t"
                f"Modelo: {self.modelo}\n\t"
                f"Cor: {self.cor}\n")

    def ligar(self):
        return print(f"O {self.nome} está Ligado!")

    def desligar(self):
        print(f"O {self.nome} está Desligado!")

    def acelerar(self):
        print(f"O {self.nome} está Acelerando!")


carro1 = Carro("Volkswagen",
               2013,
               "Golf",
               "Hatch",
               "Preto")

carro2 = Carro("Honda",
               2025,
               "Civic",
               "Sedan",
               "Vermelho")

carro3 = Carro("Toyota",
               2020,
               "Hillux SW4",
               "SUV",
               "Branca")

carro4 = Carro("Nissan",
               1999,
               "Skyline R34",
               "Sedan",
               "Azul Escuro")

carro5 = Carro("BYD",
               2025,
               "Seal",
               "Sedan",
               "Azul marinho")


carros = [carro1, carro2, carro3, carro4, carro5]

for exibir_carros in carros:
    print(exibir_carros)
