print("Questão 4: O Boletim Escolar Automático (Aritmética + Lógica AND)\n")

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
frequencia_digitada = int(input("Digite a quantidade de frequencia: "))

media = (nota1 + nota2) / 2
porcentagem_frequencia_min = (200 * 75) / 100

frequencia_do_aluno = (frequencia_digitada * 200) / 100

aprovado = (frequencia_do_aluno < 75) and (media >= 6.0)

print(f"A média do aluno foi: {media:.2f}. Ele foi aprovado: {aprovado}")



