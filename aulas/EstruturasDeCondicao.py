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
