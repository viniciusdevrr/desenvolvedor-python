import pandas as pd

dados = pd.read_csv("dados_despadronizados.csv",
                    dtype={"cpf": "string",
                           "numero": "string",
                           "salario": "string"})

cpf_limpo = (dados["cpf"]
             .str.replace(".", "", regex=False)
             .str.replace("-", "", regex=False)
             .str.replace(" ", "", regex=False))

dados["cpf_formatado"] = cpf_limpo

dados["cpf_valido"] = cpf_limpo.str.len() == 11


dados["numero_formatado"] = (dados["numero"]
                             .str.replace(r"\D", "", regex=True)
                             )

dados["numero_valido"] = dados["numero_formatado"].str.len() > 10


dados["salario_formatado"] = (dados["salario"]
                              .str.replace(r"[^\d,.\-]", "", regex=True)
                              .str.replace(r"\.(?=\d{3}(?:\.|,|$))", "", regex=True)
                              .str.replace(r",", ".", regex=False)
                              .astype(float)
                              )

dados["salario_anual"] = dados["salario_formatado"] * 12


dados = dados[[
    "nome",
    "cpf", "cpf_formatado", "cpf_valido",
    "numero", "numero_formatado", "numero_valido",
    "salario", "salario_formatado",
    "salario_anual"
]]


dados.to_csv("dados_padronizados.csv", index=False)

print(dados)