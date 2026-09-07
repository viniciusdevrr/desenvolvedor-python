print("Questão 5: Calculadora Básica de Dois Números \n")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador matemático (+, -, *, /): ").strip()

match operador:
    case "+":
        print(numero1 + numero2)
    case "-":
        print(numero1 - numero2)
    case "*":
        print(numero1 * numero2)
    case "/":
        if numero2 != 0:
            print(numero1 / numero2)
        else:
            print("Erro: Divisão por zero!")
    case _:
        print("Operação inválida!")