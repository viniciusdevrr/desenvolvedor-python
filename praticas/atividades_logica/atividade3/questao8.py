print("Questão 8: A Calculadora de Lucro da Empresa \n")

nome_produto = input("Digite o nome do produto: ")
custo_fabrica = float(input("Digite o valor do custo da fabrica: "))
preco_venda = float(input("Digite o valor do preco do venda: "))

lucro = preco_venda - custo_fabrica
verifica_lucro = lucro > 20

print("Produto: ", nome_produto, "Lucro: ", lucro, "Lucro foi bom? ", verifica_lucro)