print("Questão 3: Somador de Números \n")

soma = 0

print("Digite números inteiros (digite [0] para encerrar e ver a soma):")

while True:
    numero = int(input("Digite um número: "))

    if numero == 0:
        break
    soma += numero

print(f"\nA soma de todos os números digitados é: {soma}")