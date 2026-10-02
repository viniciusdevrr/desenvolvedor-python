def acrescentar_aluno():
    nome = input('Digite o nome do aluno: ')
    turma = input('Digite o nome da turma: ')
    bim1 = float(input('Digite a nota do primeiro bimestre: '))
    bim2 = float(input('Digite a nota do segundo bimestre: '))
    bim3 = float(input('Digite a nota do terceito bimestre: '))
    bim4 = float(input('Digite a nota do quarto bimestre: '))

    media = bim1 + bim2 + bim3 + bim4 / 4
    if media >= 7:
        print(f'Aprovado!')
    else:
        print(f'Reprovado!')

    with open("vendas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{turma};{bim1};{bim2};{bim3};{bim4};{media}\n")
    print("Aluno Cadastrado com sucesso!")

def listar_vendas():
    try:
        with open("vendas.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                # strip -> retira dos dados espaços desnecessários \n
                # split -> separa atributos que estão entre ; dentro de uma nova lista
                linha = linha.strip().split(";")
                print(f"Vendedor: {2}\n"
                      f"Produto: {linha[1]}\n"
                      f"Valor: {linha[2]}")
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except Exception as error:
        print(f"Erro inesperado: {error}")
    finally:
        print("Base de dados analisada.")

def somar_todas_as_vendas(valor_total = 0):
    with open("vendas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.strip().split(";")
            valor_produto = float(linha[2])

            valor_total += valor_produto
    return valor_total

def calcular_media_aluno():
    with open("vendas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            linha = linha.strip().split(";")
            if linha[0] == "João":
                print(f"O {linha[0]} fez a venda de {linha[1]} por {linha[2]}")

def maior_venda():
    with open("vendas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        valores_vendas = []

        for linha in linhas:
            linha = linha.strip().split(";")
            valores_vendas.append(float(linha[2]))

        maior_valor = max(valores_vendas)

        print(f'O maior valor de venda: {maior_valor}')

def menor_venda():
    with open("vendas.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        valores_vendas = []

        for linha in linhas:
            linha = linha.strip().split(";")
            valores_vendas.append(float(linha[2]))

        menor_valor = min(valores_vendas)

        print(f'O maior valor de venda: {menor_valor}')

# SIMULANDO UM SISTEMA FUNCIONAL
while True:
    finalizar = False
    print("SISTEMA DE COMPRAS\n\n")
    opcao = int(input("Escolha uma das opções\n"
                  "1) Acrescentar aluno\n"
                  "2) Calcular média do aluno\n"
                  "3) Somar todas as vendas\n"
                  "4) Ver a vendas de um vendedor\n"
                  "5) Maior venda\n"
                  "6) Menor venda\n"
                  "7) Finalizar programa\n"))

    match opcao:
        case 1:
            acrescentar_aluno()
        case 2:
            calcular_media_aluno()
        case 3:
            print(somar_todas_as_vendas())
        case 4:
            achar_vendedor()
        case 5:
            maior_venda()
        case 6:
            menor_venda()
        case _:
            print("Finalizando programa...")
            finalizar = True
            break

    if finalizar:
        break