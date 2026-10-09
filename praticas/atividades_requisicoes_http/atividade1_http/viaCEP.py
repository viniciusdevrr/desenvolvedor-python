import json
import requests

historico_pesquisa = []

cep_digitado = input("Digite o CEP: ")
link = f"https://viacep.com.br/ws/{cep_digitado}/json/"

try:
    resposta = requests.get(link)

    if resposta.status_code == 200:
        dados = resposta.json()

        historico_pesquisa.append(dados)

        with open("historico_pesquisa.json", "w", encoding="utf-8") as arquivo:
            json.dump(historico_pesquisa, arquivo, ensure_ascii=False, indent=4)
    print("Histórico adicionado no JSON com sucesso!")

except Exception as erro:
    print(erro)
