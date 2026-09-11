"""Crie uma lista que ela armazene um numero x de
funcionários. Usando o while, adicione quantos
funcionários quiser.

Com o for, você irá imprimir duas listas:
Uma lista com todos os funcionários que receberão um
aumento.
Outra lista, com todos os funcionário que serão
demitidos.

Você irá decidir qual funcionário será demitido ou
receberá aumento pelo index do funcionário lista[]"""

funcionarios = []
aumentos = []
demitidos = []

db_func = [
    funcionarios,
    aumentos,
    demitidos
]
while True:
    while True:
        add_func = input("Adicione um funcionario: ")
        funcionarios.append(funcionarios)
        break
    break

for banco in db_func:
    for index in db_func:
        if index in funcionarios:
            if index == funcionarios[0]:
                print(f"O funcionario {index} recebeu aumento")

        if index in demitidos:
            if index == demitidos[2]:
                print(f"O funcionario {index} foi demitido")












print(lista)


