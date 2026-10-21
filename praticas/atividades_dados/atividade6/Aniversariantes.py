import json

with open("base1.json", "r", encoding="utf-8") as arquivo:
    dados_base1 = json.load(arquivo)

with open("base2.json", "r", encoding="utf-8") as arquivo:
    dados_base2 = json.load(arquivo)

with open("base3.json", "r", encoding="utf-8") as arquivo:
    dados_base3 = json.load(arquivo)

lista_aniversariantes = []

for aniversariante in dados_base1:
    novo_dicionario = {
        "nome": aniversariante['nome'],
        "aniversario": aniversariante['aniversario']
    }
    lista_aniversariantes.append(novo_dicionario)

for aniversariante in dados_base2:
    novo_dicionario = {
        "nome": aniversariante['nome'],
        "aniversario": aniversariante['aniversario']
    }
    lista_aniversariantes.append(novo_dicionario)

for aniversariante in dados_base3:
    novo_dicionario = {
        "nome": aniversariante['nome'],
        "aniversario": aniversariante['aniversario']
    }
    lista_aniversariantes.append(novo_dicionario)

with open("aniversariantes.json", 'w') as arquivo:
    json.dump(lista_aniversariantes, arquivo, indent=4, ensure_ascii=False)

# Desafio Extra
lista_aniversariantes.sort(key=lambda aniversariante: aniversariante['nome'])

with open("aniversariantes.json", 'w') as arquivo:
    json.dump(lista_aniversariantes, arquivo, indent=4, ensure_ascii=False)