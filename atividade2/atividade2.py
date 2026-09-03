"""
ATIVIDADE 2
    Crie um algoritmo, que faça um formulário em que o usuário digite seu nome, sue idade
e se ele tem plano de saúde (True ou False)
    O seu sistema deve retorna em um único print(), todas as informaçoes. e se ele for menor
de idade ou idoso ou se não tiver plano de saúde, que ele não será aceito no nosso formulário;
    Exemplo de retorno: Seu nome é João, você tem 22 anos, tem plano? False. Você foi aceito? False
"""

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
plano = input("Voce tem plano de saúde? True ou False: ")

regras = (18 <= idade > 60) and (plano == True)

print("Seu nome é",nome ,", você tem 22 anos, tem plano?",plano,". Você foi aceito?", regras)
