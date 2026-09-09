print("Questão 5: Tabuada Simples \n")

numero = int(input("Digite umm numero e veja a tabuada: "))
contador = 1

print("Tabuada do: ", numero)

while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1
