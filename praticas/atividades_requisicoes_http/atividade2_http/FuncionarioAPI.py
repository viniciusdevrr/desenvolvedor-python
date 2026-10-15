import requests
import json

link_funcionarios = "http://192.168.205.100:8080/funcionarios"

#                json    python
# dados vazios = null == None

resposta = requests.get(link_funcionarios) # enviando uma requisição do tipo GET
print(resposta.json()) # mostrando o que recebeu na requisição HTTP

lista_funcionarios = resposta.json()

print("--- LISTA DE FUNCIONARIOS SEM ENDEREÇO CADASTRADO ---\n")
for funcionario in lista_funcionarios:
    if funcionario['cep'] == None:
        print(f"O funcionário(a) {funcionario['nome']} não tem cep cadastrado\n")

        while True:
            cep_digitado = input("Digite o CEP dele: ")
            if len(cep_digitado) != 8:
                print("CEP invalido")
            else:
                link_cep = f"https://viacep.com.br/ws/{cep_digitado}/json/"
                resposta = requests.get(link_cep)


            if "erro" in resposta.json():
                print(resposta.status_code)
                print("Erro")
            else:
                print(resposta.status_code)
                resposta.status_code == 200
                dicionario_funcionario = resposta.json()
                for chave, valor in dicionario_funcionario.items():
                    if chave == 'localidade':
                        funcionario['cidade'] = valor
                    if chave == 'estado':
                        funcionario['estado'] = valor
                funcionario['cep'] = cep_digitado
                break

# base de dados atualizada
for funcionario in lista_funcionarios:
    print(funcionario)

# inserir dados onde estiver algum dado vazio
# no cep, apenas aceitar CEPS válidos
#   (que tenham retorno de cidade, estado, etc...)
# salvar os dados preenchidos em um arquivo JSON
#   (ex: dados_funcionarios_atualizados.json)




with open("dados_funcionarios_atualizados.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(lista_funcionarios, arquivo_json, ensure_ascii=False, indent=4)

print(arquivo_json)