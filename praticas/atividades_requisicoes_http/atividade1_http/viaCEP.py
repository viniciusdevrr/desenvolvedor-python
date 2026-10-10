import json
import requests

print("Atividade 1 - Consulta de CEP com Python e JSON\n")

try:
    with open("historico_pesquisa.json", "r", encoding="utf-8") as arquivo:
        historico_pesquisa = json.load(arquivo)
        print("Arquivo historico_pesquisa.json carregado com sucesso!\n")
except:
    historico_pesquisa = []
    print("Arquivo não encontrado\n")

while True:
    cep_digitado = input("Digite o CEP (ou digite [fim] para finalizar e visualizar o arquivo): ")
    
    if cep_digitado == "fim":
        break

    link = f"https://viacep.com.br/ws/{cep_digitado}/json/"

    try:
        resposta = requests.get(link)

        if resposta.status_code == 200:
            novo_dado = resposta.json()
            
            if "erro" in novo_dado:
                print("CEP não encontrado ou inválido!\n")
            else:
                historico_pesquisa.append(novo_dado)
                print(f"CEP {cep_digitado} adicionado com sucesso na lista!\n")
        else:
            print("CEP não encontrado ou inválido!\n")

    except Exception as erro:
        print(erro)

with open("historico_pesquisa.json", "w", encoding="utf-8") as arquivo:
    json.dump(historico_pesquisa, arquivo, indent=4, ensure_ascii=False)
    print("Arquivo historico_pesquisa.json criado e atualizado com sucesso!\n")

with open("historico_pesquisa.json", "r", encoding="utf-8") as arquivo:
    pesquisas = json.load(arquivo)
    print("Arquivo historico_pesquisa.json para Python!\n")

    