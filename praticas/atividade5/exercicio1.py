print("ID |Produto         |Preço "
      "\n1  |Cachorro-quente |R$ 10,00 "
      "\n2  |Hambúrguer      |R$ 15,00 "
      "\n3  |Batata Frita    |R$  8,00 "
      "\n4  |Refrigerante    |R$  5,00 \n")

id_produto = input("Digite o ID do produto que você deseja: ")

match id_produto:
    case '1':
        print("Cachorro-quente |R$ 10,00 | Bom apetite.")
    case '2':
        print("Hambúrguer      |R$ 15,00 | Bom apetite.")
    case '3':
        print("Batata Frita    |R$  8,00 | Bom apetite.")
    case '4':
        print("Refrigerante    |R$  5,00 | Bom apetite.")
    case 1:
        print("Resposta não pode ser númerica.")
    case _:
        print("Resposta inválida.")

