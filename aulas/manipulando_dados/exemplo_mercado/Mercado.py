produtos = []

produtos.append("Leite")
produtos.append("Macarrão")
produtos.append("Carne")
produtos.append("Açaí")
produtos.append("Iogurte")


with open("recibo.txt", "w", encoding="utf-8") as arquivo:
    for produto in produtos:
        arquivo.write(f"{produto}\n")

with open("recibo.txt", "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

        posicao = texto.find("Iogurte")

        print(posicao)
        produto_vencido = texto[posicao:posicao+7]
        print(f"O produto {produto_vencido} esta vencido")