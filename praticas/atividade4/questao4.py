print("Questão 4: O Teste do Saldo Bancário\n")

saldo_atual = float(input("Digite o saldo atual da conta (ex: 500.00): "))
valor_saque = float(input("Digite o valor que deseja sacar: "))

if valor_saque <= saldo_atual:
    novo_saldo = saldo_atual - valor_saque
    print(f"Saque realizado com sucesso! Saldo atual: R$ {novo_saldo:.2f}.")
else:
    print("Saldo insuficiente para realizar esta operação.")