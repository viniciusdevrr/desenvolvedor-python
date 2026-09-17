print("Questão 7: O Formulário de Doação de Sangue (Múltiplas Condições) \n")

idade = int(input("Digite sua idade: "))
peso = float(input("Digite sua peso: "))

regras = (idade >= 16) and (idade <= 69) and (peso > 50)

print("Você pode doar sangue? ", regras)