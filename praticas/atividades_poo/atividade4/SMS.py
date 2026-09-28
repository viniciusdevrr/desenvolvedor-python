from Notificacao import Notificacao


class SMS(Notificacao):

    def enviar(self, destinatario, mensagem):
        print(f"Enviando SMS para o número {destinatario}")

        if len(destinatario) >= 9:
            print(f"Mensagem: '{mensagem}'")
            print("Status: SMS enviado com sucesso!")
        else:
            print("Status: ERRO! Número de telefone inválido (muito curto).")