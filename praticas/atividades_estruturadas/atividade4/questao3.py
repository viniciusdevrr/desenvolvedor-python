print("Questão 3: O Validador de Idade para Votação\n")

idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você é obrigado a votar.")
else:
    print("Você ainda não é obrigado a votar.")