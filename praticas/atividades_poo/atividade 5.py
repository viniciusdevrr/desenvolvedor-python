class ItemPedido:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        try:
            self.valor = float(valor)
        except ValueError:
            raise ValueError (f"Erro: O valor para '{self.descricao}' "
                  f"deve ser estritamente numérico.")

class Mesa:
    def __init__(self, numero_mesa):
        self.numero_mesa = numero_mesa
        self.pedidos = []

    def adicionar_pedido(self, item):
        self.pedidos.append(item)
        print(f"-> {item.descricao} adicionado à {self.numero_mesa}.")

    def somar_total(self):
        total = 0
        for pedido in self.pedidos:
            total += pedido.valor
        return total

    def fechar_conta(self, taxa_servico):
        subtotal = self.somar_total()

        valor_taxa = subtotal * (taxa_servico / 100)
        total_final = subtotal + valor_taxa

        print(f"\nExtrato da Mesa: {self.numero_mesa}")
        for item in self.pedidos:
            print(f"- {item.descricao}: R$ {item.valor}")

        print(f"\nTaxa de serviço ({taxa_servico}%) = R$ {valor_taxa:.2f}")
        print(f"Total a pagar = R$ {total_final:.2f}")

# Função auxiliar para simular a interface do sistema e capturar as exceções sem quebrar o app
def registrar_pedido_seguro(mesa, descricao, valor):
    try:
        item = ItemPedido(descricao, valor)
        mesa.adicionar_pedido(item)
    except ValueError as erro:
        print(f"ALERTA DO SISTEMA: {erro}")

# 1. Instanciando as mesas
mesa1 = Mesa("Mesa 1")

# 2. Registrando pedidos válidos
registrar_pedido_seguro(mesa1, "Pizza Margherita", 45.90)
registrar_pedido_seguro(mesa1, "Refrigerante", 8.50)

# 3. Testando o Tratamento de Exceções (Simulando erro de digitação do garçom)
print("\n--- TESTANDO ENTRADA INVÁLIDA ---")
registrar_pedido_seguro(mesa1, "Pudim", "quinze")  # Deve exibir o ALERTA DO SISTEMA e não quebrar
registrar_pedido_seguro(mesa1, "Café", "5,50")     # Erro comum de vírgula, deve acionar o ALERTA


