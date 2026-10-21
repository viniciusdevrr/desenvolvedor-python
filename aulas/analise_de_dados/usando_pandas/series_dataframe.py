import pandas as pd


nomes = ["Joao", "Felipe", "André"]
nomes_series = pd.Series(nomes)

nomes = ["Joao", "Felipe", "André"]
nomes_series = pd.Series(nomes, index=["id1", "id2", "id3"])

# DATAFRAMES
# Converter um dicionario em uma DATAFRAME (CLASSE)

notas = {
    "nome": ["Joao", "Felipe", "Bruno", "Maikon"],
    "turma": ["Python", "Java", "Banco de Dados", "Front-end"],
    "notas": [10, 8, 5, 6]
}

df = pd.DataFrame(notas,
                  index=["aluno1", "aluno2", "aluno3", "aluno4"],)
print("Atual")
print(df)
print("\nAtualizado")
df["status"] = ["Aprovado", "Aprovado", "Reprovado", "Reprovado"]
print(df)

nova_linha = pd.DataFrame([{
    "nome": "Vinicius",
    "turma": "Python",
    "notas": "10",
    "status": "Aprovado",
}], index=["aluno5"])

df = pd.concat([df, nova_linha])

print("\nAtualizado 2")
print(df)


print(df[["nome", "turma"]])

