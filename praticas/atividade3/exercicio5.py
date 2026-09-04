print("Questão 5: O Sistema de Desconto (Lógica OR)\n")

valor_compra = float(input("Digite o valor da compra: "))
cartaovip = int(input("Possui o cartao vip: Sim[1] ou Nao[0]: "))

frete = (valor_compra >= 200.00) or (cartaovip == 1)

print("Você ganhou frete grátis? ",frete)