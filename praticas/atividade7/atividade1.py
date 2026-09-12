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

while True:
    nome = input("Digite o nome do funcionário ou [sair]: ")
            
    if nome == "sair":
        break

    funcionarios.append(nome)

aumentos = []
demitidos = []

for index in range(len(funcionarios)):
    if index % 2 == 0:
        aumentos.append(funcionarios[index])
    else:
        demitidos.append(funcionarios[index])

print(f"\nFuncionários com receberam aumento: {aumentos}")
print(f"Funcionários que foram demitidos: {demitidos}")


