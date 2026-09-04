# IF e ELSE -> SE e SENÃO

#CASE SENSITIVE -> E != e
idade = int(input("Digite sua idade: "))

# criando uma condição na execução do código
if idade >= 18: # executa SE a resposta boalna for True
    if idade > 65:
        print("Desculpe senhor, voce não pode entrar nessa balada.")
    else:
        print("Voce pode entrar nessa balada.")
elif idade < 5:
    print("Alem de não poder entrar, você nao pode andar sozinho")
else:
    print("Voce nao pode entrar, é menor de idade")

print("\n")

nome = input("Digite seu nome: ")

if nome == "":
    print("Por favor digite um nome valido.")
else:
    print("Ola "+ nome +"! Seja bem vindo a nossa balada.")

# MONTANDO UMA QUESTAO DE PROVA

print("1 + 1 é igual á:\na)1\nb)2\nc)3\nd)4")
primeira_resposta = input('Digite a opção correta: ')
resposta = 'b'

#MATCH CASE

match primeira_resposta: # Espera um String
    case 'a': # primera_resposta == 'a'? False
        print("Resposta incorreta.")
    case 'b':# primera_resposta == 'b'? True
        print("Resposta correta.")
    case 'c':
        print("Resposta incorreta.")
    case 'd':
        print("Resposta incorreta.")
    case 1:
        print("Resposta não pode ser númerica.")
    case _: # _ significa valor default, ou seja, valor padrão
        print("Resposta inválida.")


# VÁRIAS OPÇÕES EM UM CASE

dia = input('Digite o dia dessa semana: ')

match dia:
    case "sabado" | "domingo":
        print("Esse dia é em um FINAL DE SEMANA")
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Esse dia é DURANTE A SEMANA")