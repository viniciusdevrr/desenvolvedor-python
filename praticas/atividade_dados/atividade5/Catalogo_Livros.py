import json

print("Atividade 5 - Sistema de Catálogo de Livros\n")

with open("catalogo.json", "r", encoding="utf-8") as arquivo:
    catalogo_livros = json.load(arquivo)
    print("Arquivo catalogo.json para Python carregado com sucesso!\n")

novos_livros = [
    {
        "id": 31,
        "nome": "Ed & Lorraine Warren: Demonologistas",
        "descricao": "A biografia definitiva dos investigadores paranormais, explorando casos reais de possessões e poltergeists.",
        "preco": 84.50,
        "em_estoque": 20
    },
    {
        "id": 32,
        "nome": "Ed & Lorraine Warren: Lugar Sombrio",
        "descricao": "Relato meticuloso sobre os fenômenos aterrorizantes enfrentados por uma família em uma antiga funerária.",
        "preco": 75.00,
        "em_estoque": 15
    },
    {
        "id": 33,
        "nome": "Ed & Lorraine Warren: Vidas Eternas",
        "descricao": "Detalha o dramático caso da família Smurl, atormentada por forças demoníacas durante três anos.",
        "preco": 90.00,
        "em_estoque": 25
    },
    {
        "id": 34,
        "nome": "O Iluminado",
        "descricao": "Clássico do terror psicológico escrito por Stephen King, ambientado no isolado e sinistro Hotel Overlook.",
        "preco": 59.90,
        "em_estoque": 30
    },
    {
        "id": 35,
        "nome": "A Sociedade do Anel",
        "descricao": "O primeiro volume da épica trilogia de fantasia O Senhor dos Anéis, escrita por J.R.R. Tolkien.",
        "preco": 69.90,
        "em_estoque": 40
    }
]

catalogo_livros.extend(novos_livros)

with open("catalogo.json", "w", encoding="utf-8") as arquivo:
    json.dump(catalogo_livros, arquivo, indent=4, ensure_ascii=False)
    print("Livros novos adicionados com sucesso e catalogo.json atualizado!\n")

valor_total_loja = 0
print("Verificando livros com menos de 15 unidades no estoque...\n")

for livro in catalogo_livros:
    if livro["em_estoque"] < 15:
        print(f"{livro['nome']} esta com ({livro['em_estoque']}) livros no estoque!")

    valor_total_estoque = livro["em_estoque"] * livro["preco"]
    valor_total_loja += valor_total_estoque

print(f"\nValor total de livros no estoque: R$ {valor_total_loja:.2f}")