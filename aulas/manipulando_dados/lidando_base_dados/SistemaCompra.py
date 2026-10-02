def cadastrar_venda():
    vendedor = input('Digite o nome do vendedor: ')
    produto = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: '))

    with open("vendas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{vendedor};{produto};{valor:.2f}\n")
    print("Venda cadastrada")

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

def achar_vendedor():
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
                  "1) Cadastrar venda nova\n"
                  "2) Listar todas as vendas\n"
                  "3) Somar todas as vendas\n"
                  "4) Ver a vendas de um vendedor\n"
                  "5) Maior venda\n"
                  "6) Menor venda\n"
                  "7) Finalizar programa\n"))

    match opcao:
        case 1:
            cadastrar_venda()
        case 2:
            listar_vendas()
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