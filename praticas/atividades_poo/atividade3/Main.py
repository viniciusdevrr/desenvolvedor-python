from Mamifero import Mamifero
from Ave import Ave

class Main:
    leao = Mamifero("Simba", 5, 70, 80)
    gaviao = Ave("Sky", 2, 75, 120)

    # 1. Tentativa de alteração direta dos atributos privados (Proteção do Encapsulamento)
    leao.__nivel_fome = -999
    leao.__idade = -10
    gaviao.__nivel_fome = -1
    gaviao.__idade = -5

    # 2. Testando ações que alteram o estado interno via Herança e Encapsulamento

    leao.correr()  # Fome sobe de 70 para 90
    gaviao.voar()  # Fome sobe de 75 para 90 (Sucesso)
    gaviao.voar()  # Fome está em 90 -> Deve exibir: "Voo negado: Sky está faminto demais para voar!"

    # 3. Testando alimentação
    leao.alimentar(50)  # Fome cai de 90 para 40
    leao.alimentar(-10)  # Deve exibir: "Erro: Porção inválida"
    
    # 4. Exibição final dos resumos
    print("\nResumo do Leao")
    leao.emitir_som()
    leao.exibir_resumo()
    print(leao.__dict__)

    print("\nResumo do Gaviao")
    gaviao.emitir_som()
    gaviao.exibir_resumo()
    print(gaviao.__dict__)
