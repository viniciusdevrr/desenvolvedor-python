import json

print("Atividade 5 - Sistema de Catálogo de Livros\n")

catalogo_livros = []

with open("banco_livros.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
        linha = linha.strip().split(";")
        catalogo_livros.append({
            "id": int(linha[0]),
            "nome": linha[1],
            "descricao": linha[2],
            "preco": float(linha[3]),
            "em_estoque": int(linha[4])
        })

with open("catalogo.json", "w", encoding="utf-8") as arquivo:
    json.dump(catalogo_livros, arquivo, indent=4, ensure_ascii=False)
    print("Arquivo catalogo.json criado com sucesso!\n")

with open("catalogo.json", "w", encoding="utf-8") as arquivo:
    catalogo_livros.append(
        {
            "id": 31,
            "nome": "Ed & Lorraine Warren: Demonologistas",
            "descricao": "A biografia definitiva dos investigadores paranormais, explorando casos reais de possessões e poltergeists.",
            "preco": 84.50,
            "em_estoque": 20
        }
    )

    json.dump(catalogo_livros, arquivo, indent=4, ensure_ascii=False)
    print(f"Livros novos adicionados com sucesso!\n")

with open("catalogo.json", "w", encoding="utf-8") as arquivo:
    json.dump(catalogo_livros, arquivo, indent=4, ensure_ascii=False)
    print(f"Arquivo catalogo.json atualizado!\n")

with open("catalogo.json", "r", encoding="utf-8") as arquivo:
    livros = json.load(arquivo)
    print("Arquivo catalogo.json para Python criado com sucesso!\n")

    valor_total_loja = 0
    print("Verificando livros com menos de 15 unidades no estoque...\n")

    for livro in livros:
        if livro["em_estoque"] < 15:
            print(f"{livro["nome"]} esta com ({livro['em_estoque']}) livros no estoque!")

        valor_total_estoque = livro["em_estoque"] * livro["preco"]
        valor_total_loja += valor_total_estoque
    print(f"\nValor total de livros no estoque: R$ {valor_total_loja:.2f}")