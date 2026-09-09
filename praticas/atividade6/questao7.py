print("Questão 7: Controle de Orçamento\n")

orcamento = 500.00

print("Saldo do seu orcamento: ", orcamento)

while orcamento > 0:
    gasto = float(input("Digite o valor do gasto: "))
    orcamento -= gasto
    print("Saldo restante: ", orcamento)

print(f"\nAtenção: Você ficou sem saldo ou estourou seu orçamento!")