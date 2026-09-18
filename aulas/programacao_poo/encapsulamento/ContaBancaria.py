# FORMA CONVENCIONAL NAO UTILIZADA NO PYTHON
class ContaBancaria: # nome da classe
    def __init__(self, titular, saldo): #metodo construtor
        self.titular = titular # self.atributo = valor do parametro
        self.__saldo = saldo #privado

    # metodo Getters e Setters (Ger = Pegar e Set = Inserir)
    # Metodos Convencionais
    def get_titular(self):
        senha = 1234
        senha_digitada = int(input("Digite sua senha para buscar titular: "))

        if senha == senha_digitada:
            return self.titular
        else:
            return "Senha incorreta!"

    def set_titular(self, novo_titular):
        senha = 1234
        senha_digitada = int(input("Digite sua senha para atualizar titular: "))

        if senha == senha_digitada:
            self.titular = novo_titular
            return "Titular atualizada!"
        else:
            return "Senha incorreta!"

# conta_banco = ContaBancaria('Vinicius', 10)
# print(conta_banco.get_titular())
#
# conta_banco.set_titular("Ciclano")
# print(conta_banco.get_titular())

# METODO UTILIZADO NO PYTHON
class ContaBancariaCorreta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    @property # Anotation -> anotaçao
    def saldo(self): # Criando um GET
        return self.__saldo

    @saldo.setter # Criando um SET novo no metodo
    def saldo(self, novo_saldo):
        if novo_saldo < 0:
            print("Não é possivel colocar saldo negativo!")
        else:
            print(f"Saldo atual: {novo_saldo}")
            self.__saldo = novo_saldo

    def sacar(self, valor_saque):
        if valor_saque <= self.__saldo:
            print(f"Quantidade retirada: {valor_saque}")
            self.saldo -= valor_saque
            print("Saldo restante: R$", self.__saldo)
        else:
            print(f"Valor de saque {valor_saque}")
            print(f"Saldo atual: {valor_saque}")
            print("Saldo insuficiente!")

    def transferir(self, valor_transfer):
        if valor_transfer <= self.__saldo:
            self.__saldo -= valor_transfer
        else:
            print(f"Valor da transferencia: {valor_transfer}")
            print(f"Saldo atual: {self.__saldo}")
            print("Saldo insuficiente!")

usuario_banco_correto = ContaBancariaCorreta("Vinicius", 10000)
print(usuario_banco_correto.saldo)

usuario_banco_correto.saldo = -20000

usuario_banco_correto.sacar(1000)

usuario_banco_correto.transferir(50000)