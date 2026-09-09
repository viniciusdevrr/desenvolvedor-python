print("Questão 4: Menu Interativo \n")

while True:
    print("1 - Mostrar saudação")
    print("2 - Sair do programa")
    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        print("Ola, seja bem muito bem-vindo(a)!\n")
    elif opcao == 2:
        print("Programa encerrado!")
        break
    else:
        print("Opcao invalida!\n")

