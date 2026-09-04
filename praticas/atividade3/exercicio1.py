print("Questão 1: A Divisão da Conta (Calculadora) \n")

valor_conta = float(input('Digite o da valor conta: '));
qtd_pessoas = int(input("Quantas pessoas tem na mesa: "));

valor_dividido = valor_conta / qtd_pessoas;
print("O valor total foi de R$", valor_conta,", e cada pessoa deve pagar R$", valor_dividido);