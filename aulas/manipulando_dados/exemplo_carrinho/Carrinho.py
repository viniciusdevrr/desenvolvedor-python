carrinho = []
total = 0

while True:
    nome = input("Digite o nome do produto ou fim para sair: ")

    if nome == "fim":
        break

    preco = float(input("Digite o preco: "))
    carrinho.append([nome, preco])

    total += preco

with open("carrinho.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("--- Recibo do Carrinho ---\n\n")

    for produto in carrinho:
        nome_produto = produto[0]
        preco_produto = produto[1]

        arquivo.write(f"Produto: {nome_produto} R$ {preco_produto:.2f}\n")

    arquivo.write(f"\nTotal a pagar: R$ {total:.2f}")

print("Compra finalizada e recibo salvo com sucesso!")