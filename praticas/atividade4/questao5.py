print("Questão 5: A Catraca VIP de Eventos\n")

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
vip = int(input("Você possui convite VIP? (Digite 1 para Sim, 0 para Não): "))
organizador = int(input("Você é um dos organizadores? (Digite 1 para Sim, 0 para Não): "))

if (idade >= 18 and vip == 1) or organizador == 1:
    print("Entrada PERMITIDA! Seja bem-vindo", nome)
else:
    print("Entrada NEGADA! Você não atende aos requisitos.")