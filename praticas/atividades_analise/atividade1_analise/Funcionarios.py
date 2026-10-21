import pandas as pd

df = pd.read_csv("funcionarios.csv", sep=";")

print("\nSalarios menores que 3000:")
print(df[df['salario'] < 3000])

print("\nSalarios maiores que 5000:")
print(df[df['salario'] > 5000])

print("\nSalarios iguais a 3100:")
print(df[df['salario'] == 3100])

print("\nCargos: Analista de Dados / Analista de Sistemas / Desenvolvedor Java / Cientista de Dados")
print(df[
          (df["cargo"] == "Analista de Dados") |
          (df["cargo"] == "Analista de Sistemas") |
          (df["cargo"] == "Desenvolvedor Java") |
          (df["cargo"] == "Cientista de Dados")
      ])

print("\nNomes,Cargos e Salarios maiores que 6000:")
print(df[df["salario"] > 6000][["nome", "cargo", "salario"]])


print("\nFuncionarios com id [par]:")
print(df[df["id"] % 2 == 0])