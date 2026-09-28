from Notificacao import Notificacao


class Email(Notificacao):

    def enviar(self, destinatario, mensagem):
        print(f"Enviando Email para {destinatario}")
        print(f"Mensagem: '{mensagem}'")
        print("Status: E-mail enviado com sucesso!")