import json
import requests

link_funcionarios = "http://192.168.205.100:8080/funcionarios"

resposta = requests.get(link_funcionarios)
lista_funcionarios = resposta.json()

print("--- LISTA DE FUNCIONARIOS SEM ENDEREÇO CADASTRADO ---\n")

for funcionario in lista_funcionarios:
    if funcionario['cep'] == None:
        print(f"O funcionário(a) {funcionario['nome']} não tem cep cadastrado\n")
        while True:
            try:
                cep_digitado = input("Digite o CEP dele: ")
                link_cep = f"https://viacep.com.br/ws/{cep_digitado}/json/"
                resposta = requests.get(link_cep)
                print(resposta.status_code)
                if resposta.status_code == 200:
                    dicionario_funcionario = resposta.json()

                    funcionario['cep'] = cep_digitado
                    funcionario['cidade'] = dicionario_funcionario['localidade']
                    funcionario['estado'] = dicionario_funcionario['estado']
                    break
                else:
                    print("CEP digitado incorretamente")
            except Exception as erro:
                print("CEP digitado invalido, não tem endereço")

with open("dados_funcionarios_atualizados.json", "w", encoding="utf-8") as arquivo_json:
  json.dump(lista_funcionarios, arquivo_json, ensure_ascii=False, indent=4)

print("Arquivo salvo com sucesso!")