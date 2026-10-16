import requests, json

with open("dados_funcionarios_atualizados.json", "r", encoding="utf-8") as arquivo_json:
    lista_funcionarios = json.load(arquivo_json)

    for funcionario in lista_funcionarios:
        id_funcionario = funcionario["id"]
        novo_dicionario = {
            "cargo": funcionario["cargo"],
            "cep": funcionario["cep"],
            "cidade": funcionario["cidade"],
            "estado": funcionario["estado"],
            "id": id_funcionario,
            "nome": funcionario["nome"],
            "salario": funcionario["salario"],
            "tempoEmpresa": funcionario["tempoEmpresa"],
        }

    atualizacao = requests.put(f"http://192.168.205.100:8080/funcionarios/{id_funcionario}",
                               json=novo_dicionario)
    print(atualizacao) # PRECISAM SER 200 DE FORMA OBRIGATÓRIA
    busca = requests.get(f'http://192.168.205.100:8080/funcionarios')
    for funcionario in busca.json():
        print(funcionario)
