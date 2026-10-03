def acrescentar_aluno():
    try:
        nome = input("Digite o nome do aluno: ")
        turma = input("Digite a turma: ")
        bim1 = float(input("Digite a nota do primeiro bimestre: "))
        bim2 = float(input("Digite a nota do segundo bimestre: "))
        bim3 = float(input("Digite a nota do terceiro bimestre: "))
        bim4 = float(input("Digite a nota do quarto bimestre: "))

        media = (bim1 + bim2 + bim3 + bim4) / 4
        if media >= 7:
            status = "Aprovado"
        else:
            status = "Reprovado"

        with open("alunos.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"\n{nome};{turma};{bim1};{bim2};{bim3};{bim4};{status}")
        print("Aluno Cadastrado com sucesso!")

    except FileNotFoundError:
        print("Arquivo não encontrado ou não existe.")
    except Exception as error:
        print(f"Erro inesperado: {error}")

def calcular_media_aluno():
    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            nome = input("Digite o nome do aluno: ")

            encontrado = False
            for linha in linhas:
                linha = linha.strip().split(";")

                if linha[0] == nome:
                    media = (float(linha[2]) + float(linha[3]) + float(linha[4]) + float(linha[5])) / 4
                    print(f"A média de {nome} é {media:.2f}.")
                    break

            if not encontrado:
                print("Aluno não encontrado!")

    except FileNotFoundError:
        print("Arquivo não encontrado ou não existe.")
    except Exception as error:
        print(f"Erro inesperado: {error}")

def consultar_status_aluno():
    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            nome = input("Digite o nome do aluno: ").strip()

            encontrado = False
            for linha in linhas:
                linha = linha.strip().split(";")

                if linha[0] == nome:
                    print(f"Status: {linha[6]}")
                    break

            if not encontrado:
                print("Aluno não encontrado!")

    except FileNotFoundError:
        print("Arquivo não encontrado ou não existe.")
    except Exception as error:
        print(f"Erro inesperado: {error}")

def maior_media_turma():
    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            medias = []
            turma = input("Digite a turma [101, 102, 103, 104]: ").strip()

            encontrado = False
            for linha in linhas:
                linha = linha.strip().split(";")

                if linha[1] == turma:
                    media = (float(linha[2]) + float(linha[3]) + float(linha[4]) + float(linha[5])) / 4
                    medias.append(media)
                    encontrado = True

            if encontrado:
                maior_media = max(medias)
                print(f"O maior media da turma {turma} é {maior_media}")
            else:
                print("Turma não encontrada ou sem alunos cadastrados!")

    except FileNotFoundError:
        print("Arquivo não encontrado ou não existe.")
    except Exception as error:
        print(f"Erro inesperado: {error}")


while True:
    finalizar = False
    print("Sistema de Gestão Escolar\n")
    opcao = int(input("Escolha uma das opções:\n"
                  "1) Acrescentar um aluno\n"
                  "2) Calcular média do aluno\n"
                  "3) Consultar status do aluno\n"
                  "4) Verificar maior média da turma\n"
                  "5) Finalizar programa\n"
                    "= "))

    match opcao:
        case 1:
            acrescentar_aluno()
        case 2:
            calcular_media_aluno()
        case 3:
            consultar_status_aluno()
        case 4:
            maior_media_turma()
        case _:
            print("Finalizando programa...")
            finalizar = True
            break

    if finalizar:
        break