from Email import Email
from SMS import SMS
from Notificacao import Notificacao

# 1. Tentativa de instanciar a Classe Abstrata (DEVE GERAR ERRO)
# Descomente a linha abaixo para testar e provar que o Python bloqueia:
# objeto_generico = Notificacao()

# 2. Instanciando as Classes Filhas
obj1 = Email()
obj2 = SMS()

# 3. Criando um Lote de Processamento (Lista)
lote = [obj1, obj2, obj1] # Pode repetir tipos

# 4. Processando em lote (Demonstrando o Polimorfismo e a Abstração)
print("\n--- INICIANDO PROCESSAMENTO EM LOTE ---")
for item in lote:
    item.registrar_log()
    # Chama o metodo que era abstrato, mas agora está implementado
    item.enviar("ciclano@gmail.com", "Ola ciclano")
    item.enviar("1234567897", "Ola, tudo bem?")
    item.enviar("fulano@gmail.com", "Ola fulano")
    print("-" * 30)