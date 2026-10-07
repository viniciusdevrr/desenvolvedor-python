import json

print("Atividade 5 - Sistema de Catálogo de Livros\n")

catalogo_livros = []

with open("banco_livros.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
        linha = linha.strip().split(";")
        print(linha)
        livros = {
            "id": linha[0],
            "nome": linha[1],
            "descricao": linha[2],
            "preco": linha[3],
            "em_estoque": linha[4]
        }
        catalogo_livros.append(livros)

print(f"\nLivros Adicionados no dicionario: {catalogo_livros}")

with open("catalogo.json", "w", encoding="utf-8") as arquivo:
    json.dump(catalogo_livros, arquivo, indent=4, ensure_ascii=False)
    print("Arquivo de catalogo de livros criado!")


catalogo_livros.append(
    {
        "id": 31,
        "nome": "Ed & Lorraine Warren: Demonologistas",
        "descricao": "A biografia definitiva dos investigadores paranormais, explorando casos reais de possessões e poltergeists.",
        "preco": 84.50,
        "em_estoque": 20
    }
)

catalogo_livros.append(
    {
        "id": 32,
        "nome": "Ed & Lorraine Warren: Lugar Sombrio",
        "descricao": "Relato meticuloso sobre os fenômenos aterrorizantes enfrentados por uma família em uma antiga funerária.",
        "preco": 75.00,
        "em_estoque": 15
    }
)

catalogo_livros.append(
    {
        "id": 33,
        "nome": "Ed & Lorraine Warren: Vidas Eternas",
        "descricao": "Detalha o dramático caso da família Smurl, atormentada por forças demoníacas durante três anos.",
        "preco": 90.00,
        "em_estoque": 25
    }
)

catalogo_livros.append(
    {
        "id": 34,
        "nome": "O Iluminado",
        "descricao": "Clássico do terror psicológico escrito por Stephen King, ambientado no isolado e sinistro Hotel Overlook.",
        "preco": 59.90,
        "em_estoque": 30
    }
)

catalogo_livros.append(
    {
        "id": 35,
        "nome": "A Sociedade do Anel",
        "descricao": "O primeiro volume da épica trilogia de fantasia O Senhor dos Anéis, escrita por J.R.R. Tolkien.",
        "preco": 69.90,
        "em_estoque": 40
    }
)

with open("catalogo.json", "w", encoding="utf-8") as arquivo:
    json.dump(catalogo_livros, arquivo, indent=4, ensure_ascii=False)
    print("Arquivo de catalogo de livros atualizado!")