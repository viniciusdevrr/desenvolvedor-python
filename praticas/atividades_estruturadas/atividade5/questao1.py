print("Questão 1: Menu da Lanchonete \n")

print("Código |Produto         |Preço "
      "\n  1    |Cachorro-quente |R$ 10,00 "
      "\n  2    |Hambúrguer      |R$ 15,00 "
      "\n  3    |Batata Frita    |R$  8,00 "
      "\n  4    |Refrigerante    |R$  5,00 \n")

id_produto = input("Digite o código do produto que você deseja ( 1 a 4 ): ")

match id_produto:
    case '1':
        print("Cachorro-quente | R$ 10,00 ")
    case '2':
        print("Hambúrguer | R$ 15,00 ")
    case '3':
        print("Batata Frita | R$ 8,00 ")
    case '4':
        print("Refrigerante | R$ 5,00 ")
    case _:
        print("Código inválido.")

