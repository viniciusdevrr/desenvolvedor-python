class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            print("METODO: ADICIONAR_ESTOQUE")
            print(f"Quantidade no estoque: {self.__quantidade_estoque}")
            print(f"Quantidade adicionada: {quantidade}")
            self.__quantidade_estoque += quantidade
            print(f"Estoque Atualizado: {self.__quantidade_estoque}\n")
        else:
            print("Erro: Quantidade inválida\n")

    def realizar_venda(self, quantidade):
        if quantidade <= self.__quantidade_estoque:
            print("METODO: REALIZAR_VENDA")
            print(f"Quantidade no estoque: {self.__quantidade_estoque}")
            self.__quantidade_estoque -= quantidade
            print(f"Quantidade vendida: {quantidade}")
            print(f"Venda aprovada!\n")
        else:
            print(f"Venda negada. Estoque insuficiente\n")

    def aplicar_desconto(self, percentual):
        if percentual <= 80:
            print("METODO: APLICAR_DESCONTO")
            self.__preco = self.__preco * (percentual / 100)
            print(f"{self.__nome} com {percentual}% de desconto por apenas R${self.__preco:.2f}\n")

        else:
            print(f"Erro: Desconto inválido\n")

    def exibir_resumo(self):
        return print(f"METODO: EXIBIR_RESUMO\n"
                f"Nome: {self.__nome}\n"
                f"Preço: R$ {self.__preco}\n"
                f"Qtd. Estoque: {self.__quantidade_estoque}\n")

novo_produto = Produto("Coca Cola 2 Litros", 15.00, 50)


# Testando metodo adicionar_estoque;
novo_produto.adicionar_estoque(100)
novo_produto.adicionar_estoque(-100)
# Testando metodo aplicar_desconto;
novo_produto.aplicar_desconto(50)
novo_produto.aplicar_desconto(90)
# Testando metodo adicionar_estoque;


# 1. Tente forçar a alteração direta dos atributos
# (O Python permite criar variável fora, mas não altera a original):
novo_produto.__quantidade_estoque = -99
novo_produto.__preco = -999

# 2. Tente realizar uma venda absurdamente maior do que o estoque que
# você cadastrou inicialmente:
novo_produto.realizar_venda(25)
novo_produto.realizar_venda(200)

# 3. Exiba o resumo final. O estoque e o preço reais não podem
# ter sido afetados pelos testes maliciosos acima!
novo_produto.exibir_resumo()
print(novo_produto.__dict__)