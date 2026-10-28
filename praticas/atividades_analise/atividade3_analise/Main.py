import pandas as pd

dados = pd.read_csv("dados_despadronizados.csv",
                    dtype={"cpf": "string",
                           "numero": "string",
                           "salario": "string"})


dados.insert(2, "cpf_formatado", dados["cpf"].str.replace(r"\D", "", regex=True))
dados.insert(3, "cpf_validado", dados["cpf_formatado"].str.fullmatch(r"\d{11}"))

dados_salario_formatado = (dados["salario"]
                              .str.replace(r"[^\d,.\-]", "", regex=True)
                              .str.replace(r"\.(?=\d{3}(?:\.|,|$))", "", regex=True)
                              .str.replace(r",", ".", regex=False)
                              )

dados_salario_formatado = pd.to_numeric(dados_salario_formatado, errors="coerce")
dados.insert(6, "salario_formatado", dados_salario_formatado)

dados_numero_formatado = (
    dados["numero"].str.replace(r"\D", "", regex=True)
)

dados.insert(7, "numero_formatado", dados_numero_formatado)
dados["numero_validado"] = (dados['numero_formatado'].str.fullmatch(r"\d{10,13}"))

dados["salario_anual"] = dados["salario_formatado"] * 12

dados.to_csv("dados_padronizados.csv", index=False)

print(dados)