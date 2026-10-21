import csv, pandas as pd

df = pd.read_csv("funcionarios.csv", sep=";")

# print("\nSalarios menores que 3000:")
# print(df[df['salario'] < 3000])
#
# print("\nSalarios maiores que 5000:")
# print(df[df['salario'] > 5000])
#
# print("\nSalarios iguais a 3100:")
# print(df[df['salario'] == 3100])

# print("Cargos: Analista de Dados / Analista de Sistemas / Desenvolvedor Java / Cientista de Dados")
# print(df[
#           (df["cargo"] == "Analista de Dados") |
#           (df["cargo"] == "Analista de Sistemas") |
#           (df["cargo"] == "Desenvolvedor Java") |
#           (df["cargo"] == "Cientista de Dados")
#       ])

print(df[["nome", "cargo", "salario"]])