print("Atividade 1: Sistema de Carrinho de Compras e Pagamento")

carrinho = []
total = 0.0

# 1. Solicitando nome do usuário
usuario = input("Digite seu nome para iniciar a compra: ")

# 2. Loop de inserção de produtos no carrinho
while True:
    nome = input("Digite o nome do produto ou 'fim' para sair: ")

    if nome == "fim":
        break

    preco = float(input("Digite o preco: "))
    carrinho.append([nome, preco])
    total += preco

print("\n--- FINALIZANDO COMPRA ---")

# 3. Geração do arquivo pagamento.txt (Corrigido conforme o enunciado)
with open("pagamento.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Cliente: {usuario}\n")
    arquivo.write("RECIBO DO CARRINHO\n\n")

    for produto in carrinho:
        nome_produto = produto[0]
        preco_produto = produto[1]
        arquivo.write(f"Produto: {nome_produto}\n"
                      f"Preco do Produto: R$ {preco_produto:.2f}\n")

    arquivo.write(f"\nTotal: R$ {total:.2f}")

# 4. Leitura e exibição final de pagamento
with open("pagamento.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    print(texto)

print("\n--- PROCESSANDO PAGAMENTO ---")

termo_busca = f"Total: R$ {total:.2f}"

if termo_busca in texto:
    valor = f"{total:.2f}"
else:
    valor = "Não encontrado"

print(f"Compra processada com sucesso! Valor cobrado: R$ {valor}")