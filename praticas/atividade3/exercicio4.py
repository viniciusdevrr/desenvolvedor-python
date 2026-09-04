print("Questão 4: O Boletim Escolar Automático (Aritmética + Lógica AND)\n")

nome = input("Digite o nome seu nome: ")
nota1 = float(input("Digite sua nota 1: "))
nota2 = float(input("Digite sua nota 2: "))
media = (nota1 + nota2) / 2

frequencia = int(input("Digite a porcetagem de frequencia: "))

resultado = (media >= 6.0) and (frequencia >= 75)

print(resultado)



