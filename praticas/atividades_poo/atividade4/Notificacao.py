from abc import ABC, abstractmethod


class Notificacao(ABC):

    def registrar_log(self):
        print(" [SISTEMA] Iniciando envio de notificação...")

    @abstractmethod
    def enviar(self, destinatario, mensagem):
        pass