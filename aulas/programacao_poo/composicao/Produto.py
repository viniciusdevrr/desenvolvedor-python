class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        print(f"{self.nome} {self.preco}")

class Pedido:
    def __init__(self):
        self.pedidos = []

    def adicionar_produto(self, produto):
        self.pedidos.append(produto)

    def listar_produtos(self):
        try:
            for item in self.pedidos:
                print(item.nome, item.valor)
        except Exception as erro:
            print(f"Unexpected error: {erro}")


produto1 = Produto("Liquidificador", 100.00)
produto2 = Produto("Geladeira", 2500.00)
produto3 = Produto("Cama Casal", 1500.00)

pedido1 = Pedido()

pedido1.adicionar_produto(produto1)
pedido1.adicionar_produto(produto2)
pedido1.adicionar_produto(produto3)

pedido1.listar_produtos()
