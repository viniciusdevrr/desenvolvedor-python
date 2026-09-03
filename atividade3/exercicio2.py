print("Questão 2: A Fábrica de Caixas (Operador de Módulo) \n");

total_macas = int(input("Digite a quantidade total de maçãs "
                        "colhidas no dia: "))
sobras = total_macas % 12
caixas = total_macas // 12

print("Sobrarão", sobras,"maçãs fora das caixas.")
print(caixas)