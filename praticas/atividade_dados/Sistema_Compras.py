print("Questão 1: Sistema de Carrinho de Compras e Pagamento\n")

carrinho = []
total = 0

nome_cliente = input("Digite o seu nome: ")
print(f"Carrinho de compras do Cliente: {nome_cliente}\n")

while True:
    nome = input("Digite o nome do produto ou fim para sair: ")

    if nome == "fim":
        break

    preco = float(input("Digite o preco: "))
    carrinho.append([nome, preco])

    total += preco

with open("carrinho.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Recibo do Carrinho do {nome_cliente}\n")

    for produto in carrinho:
        nome_produto = produto[0]
        preco_produto = produto[1]

        arquivo.write(f"Produto: {nome_produto}\n"
                      f"Preco do Produto: R$ {preco_produto}\n")

    arquivo.write(f"\nTotal a pagar: R$ {total:.2f}")

print("Compra finalizada e recibo salvo com sucesso!")


