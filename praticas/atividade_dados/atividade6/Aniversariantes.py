print("Atividade 6 - Consolidação e Filtragem de Dados de Funcionários")

import json

with open("base1.json") as arquivo:
    dados1 = json.load(arquivo)

with open("base2.json") as arquivo:
    dados2 = json.load(arquivo)

with open("base3.json") as arquivo:
    dados3 = json.load(arquivo)

lista_aniversariantes = []

