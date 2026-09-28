from abc import ABC, abstractmethod


class Notificacao(ABC):

    def registrar_log(self):
        print(" [SISTEMA] Iniciando envio de notificação...")

    @abstractmethod
    def enviar(self, destinatario, mensagem):
        pass


class Email(Notificacao):

    def enviar(self, destinatario, mensagem):
        print(f"Enviando Email para {destinatario}")
        print(f"Mensagem: '{mensagem}'")
        print("Status: E-mail enviado com sucesso!")


class SMS(Notificacao):

    def enviar(self, destinatario, mensagem):
        dest_str = str(destinatario)
        print(f"Enviando SMS para o número {dest_str}")

        if len(dest_str) >= 9:
            print(f"Mensagem: '{mensagem}'")
            print("Status: SMS enviado com sucesso!")
        else:
            print("Status: ERRO! Número de telefone inválido (muito curto).")


# 1. Tentativa de instanciar a Classe Abstrata (DEVE GERAR ERRO)
# Descomente a linha abaixo para testar e provar que o Python bloqueia:
# objeto_generico = Notificacao()

# 1. Instanciando as Classes Filhas
obj_email = Email()
obj_sms = SMS()

# 3. Criando um Lote de Processamento (Lista)
lote = [
    (obj_email, "usuario@email.com", "Ola, usuario!"),
    (obj_sms, 11987654321, "Ola, tudo bem."),
    (obj_email, "ciclano@email.com", "Ola, ciclano!")
]

# 4. Processando em lote (Demonstrando o Polimorfismo e a Abstração)
print("\n--- INICIANDO PROCESSAMENTO EM LOTE ---")
for notificacao, destinatario, mensagem in lote:
    notificacao.registrar_log()

    # Chama o metodo que era abstrato, mas agora está implementado
    notificacao.enviar(destinatario, mensagem)

    print("-" * 30)