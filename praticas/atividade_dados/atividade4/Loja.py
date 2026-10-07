import json

print("Atividade 4 - Sistema de Gerenciamento de Estoque\n")

dicionario_loja = {
    "nome": "Tech Store",
    "produtos": [
        {
            "nome": "Teclado Mecânico RGB",
            "preco": 280.00,
            "quantidade": 25
        },
        {
            "nome": "Mousepad 90cm Itachi Uchiha",
            "preco": 80.00,
            "quantidade": 20
        },
        {
            "nome": "Mouse Logitech G Pro",
            "preco": 300.00,
            "quantidade": 30
        },
    ]
}

with open("estoque.json", "w", encoding="utf-8") as arquivo:
    json.dump(dicionario_loja, arquivo, indent=4, ensure_ascii=False)
    print("Transformando dicionario em arquivo json!\n")

# json.load
with open("estoque.json", "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)

    for produto in dados_lidos["produtos"]:
        print(f"O {produto["nome"]} custa R$ {produto["preco"]:.2f}")

with open("estoque.json", "w", encoding="utf-8") as arquivo:
    dados_lidos["produtos"].append(
        {
            "nome": "Headset Gamer Redragon",
            "preco": 150.00,
            "quantidade": 15
        })

    print(f"\nUm novo produto foi adicionado com sucesso!\n")
    for produto in dados_lidos["produtos"]:
        print(f"{produto["nome"]}\n"
              f"Valor R$ {produto["preco"]}\n"
              f"Qtd no Estoque: {produto["quantidade"]}\n")

# Desafio Extra
for produto in dados_lidos["produtos"]:
    if produto["nome"] == "Teclado Mecânico RGB":
        desconto = 0.10 * produto["preco"]
        produto["preco"] = produto["preco"] - desconto

print(f"Agora o Teclado Mecânico RGB ganhou desconto de 10% ! \n")

with open("estoque.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_lidos, arquivo, indent=4, ensure_ascii=False)

    for produto in dados_lidos["produtos"]:
        if produto["nome"] == "Teclado Mecânico RGB":
            print(f"{produto["nome"]}\n"
                  f"Valor R$ {produto["preco"]}\n"
                  f"Qtd no Estoque: {produto["quantidade"]}\n")



