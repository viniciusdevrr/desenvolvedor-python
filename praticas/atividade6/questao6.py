print("Questão 6: Jogo da Adivinhação com Tentativas \n")

num_secret = 27
tentativas = 1

print("Tente adivinhar o numero que estou pensando!")

while True:
    numero = int(input("Digite outro número: "))

    if numero != num_secret:
        print("Errouuuu")
    elif numero == num_secret:
        break
    tentativas += 1


print(f"Parabéns! Você acertou o número secreto em [{tentativas}] tentativas!")