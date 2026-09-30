print("Questão 1: Sistema de Carrinho de Compras e Pagamento")

carrinho = []
total = 0.0

# 1. Solicitando nome do usuário
usuario = input("Digite seu nome para iniciar a compra: ")

# 2. Loop de inserção de produtos no carrinho
while True:
    nome = input("Digite o nome do produto ou 'fim' para sair: ")

    if nome.lower() == "fim":
        break

    preco = float(input("Digite o preco: "))
    carrinho.append([nome, preco])
    total += preco

print("\n--- FINALIZANDO COMPRA ---")

# 3. Geração do arquivo pagamento.txt
with open("carrinho.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Cliente: {usuario}\n")
    arquivo.write("RECIBO DO CARRINHO\n\n")

    for produto in carrinho:
        nome_produto = produto[0]
        preco_produto = produto[1]
        arquivo.write(f"Produto: {nome_produto}\n"
                      f"Preco do Produto: R$ {preco_produto:.2f}\n")

    arquivo.write(f"\nTotal: R$ {total:.2f}")



with open("carrinho.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    print(texto)

    # 4. Leitura e exibição final de pagamento
    print("\n--- PROCESSANDO PAGAMENTO ---")

    termo_busca = f"R$ {total:.2f}"
    posicao = texto.find(termo_busca)

    if posicao != -1:
        valor = texto[posicao + 3: posicao + 3 + len(f"{total:.2f}")]
    else:
        valor = f"{total:.2f}"

    print(f"Compra processada com sucesso! Valor cobrado: R$ {valor}")