import pandas as pd

# Como ler um arquivo csv e buscar dados especificos
df = pd.read_csv("funcionarios.csv", sep=";")
salario_alto = df[df["salario"] > 6000]

# Transformar os dados especificos em um arquivo csv
salario_alto.to_csv("cargos_altos.csv", sep=";", index=False)
df_filtro = pd.read_csv("cargos_altos.csv", sep=";")
print(f"Original\n {df_filtro}\n")

# Como criar novos dados
novos_funcionarios = pd.DataFrame([
    {"id": 31, "nome": "Roberto Carlos", "salario": 6000.0, "cargo": "Especialista em IA"},
    {"id": 32, "nome": "Tatiane Souza", "salario": 6400.0, "cargo": "Desenvolvedor Python"}
])

# Como adicionar esses novos dados no arquivo novo csv
df_novo_funcionario = pd.DataFrame(novos_funcionarios)
df_filtro = pd.concat([df_filtro, df_novo_funcionario], ignore_index=True)
print(f"Adicionando dois funcionarios\n {df_filtro}\n")

# Como remover os dois primeiros funcionários (índices 0 e 1)
df_filtro = df_filtro.drop(index=0)
df_filtro = df_filtro.drop(index=1)
print(f"Excluindo\n {df_filtro}\n")

# Como criar uma nova coluna
df_filtro["tempo_empresa"] = [
    72, 66, 50, 25, 60
]
print(f"Nova Coluna\n {df_filtro}\n")

# Adicionar um novo funcionário com o cargo de Estagiário
estagiario = pd.DataFrame([
    {"id": 33, "nome": "Vinicius Estagiário", "salario": 2200.0, "cargo": "Estagiário", "tempo_empresa": 6}
])

df_estagiario = pd.DataFrame(estagiario)
df_filtro = pd.concat([df_filtro, df_estagiario], ignore_index=True)
print(f"Adicionando estagiario\n {df_filtro}\n")

df_filtro.to_csv("cargos_altos.csv", sep=";", index=False)