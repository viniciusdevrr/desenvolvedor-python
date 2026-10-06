import json

print("Atividade 4 - Sistema de Gerenciamento de Estoque\n")

dicionario_loja = {
    "nome": "Uefa Champions Store",
    "produtos": [
        {
            "nome": "Camisa do Barcelona 26/27",
            "preco": 200.00,
            "quantidade": 30
        },
        {
            "nome": "Camisa do Real Madrid 26/27",
            "preco": 200.00,
            "quantidade": 30
        },
        {
            "nome": "Camisa do Bayern de Munich 26/27",
            "preco": 200.00,
            "quantidade": 30
        },
    ]
}

with open("estoque.json", "w", encoding="utf-8") as arquivo:
    json.dump(dicionario_loja, arquivo, indent=4, ensure_ascii=False)
    print("Arquivo salvo com sucesso!\n")

with open("estoque.json", "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)

for lido in dados_lidos["produtos"]:
    print(f"{lido["nome"]}\n"
          f"Valor R$ {lido["preco"]}\n"
          f"Qtd no Estoque: {lido["quantidade"]}\n")

dados_lidos["produtos"].append(
    {
        "nome": "Camisa do Liverpool 26/27",
        "preco": 200.00,
        "quantidade": 30
    })

# Desafio Extra
for lido in dados_lidos["produtos"]:
    if lido["nome"] == "Camisa do Barcelona 26/27":
        desconto = 0.10 * lido["preco"]
        lido["preco"] = lido["preco"] - desconto

print(f"A Camisa do Barcelona 26/27 ganhou desconto de 10% \n")

with open("estoque.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_lidos, arquivo, indent=4, ensure_ascii=False)
    print("Arquivo atualizado com sucesso!\n")

    for lido in dados_lidos["produtos"]:
        print(f"{lido["nome"]}\n"
              f"Valor R$ {lido["preco"]}\n"
              f"Qtd no Estoque: {lido["quantidade"]}\n")


