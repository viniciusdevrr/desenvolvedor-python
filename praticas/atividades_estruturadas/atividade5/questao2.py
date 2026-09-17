print("Questão 2: Classificador de Vogais e Consoantes \n")

letra = input("Digite uma única letra do alfabeto: ")

match letra:
    case "a" |  "e" |  "i" |  "o" |  "u" :
        print("Voce digitou uma vogal.")
    case _:
        print("Não é uma vogal.")