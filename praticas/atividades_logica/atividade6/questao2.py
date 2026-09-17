print("Questão 2: Validação de Senha \n")

senha = int(input("Digite a senha: "))

while senha != 123456:
    print("Senha incorreta. Tente novamente.")
    senha = int(input("Digite senha novamente: "))

print("Acesso permitido!")