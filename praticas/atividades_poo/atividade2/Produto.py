class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    def adicionar_estoque(self, quantidade):
        quantidade = int(input("Quantidade adicionada no estoque: "))
        if quantidade > 0:
            print(f"Quantidade adicionada: {quantidade}")
            self.__quantidade_estoque += quantidade
            print(f"Estoque Atualizado: {self.__quantidade_estoque}")
        else:
            print("Erro: Quantidade inválida")

    # def realizar_venda(self, quantidade):
    #     quantidade = int(input("Quantidade retirada do estoque: "))
    #     if quantidade <= self.__quantidade_estoque:
    #         self.__quantidade_estoque -= quantidade
    #         print(f"Quantidade retirada: {quantidade}")
    #         print(f"Venda aprovada!")
    #     else:
    #         print(f"Venda negada. Estoque insuficiente")
    #
    # def aplicar_desconto(self, percentual):
    #     percentual = int(input("Percentual de desconto: "))
    #     if percentual <= 80:
    #         desconto = self.__preco * (percentual / 100)
    #         print(f"Valor atual: {self.__preco}")
    #         print(f"Desconto aplicado: {desconto}")

print("testando")

