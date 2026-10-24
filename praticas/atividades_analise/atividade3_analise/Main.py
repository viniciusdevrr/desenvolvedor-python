import pandas as pd

dados = pd.read_csv("dados_despadronizados.csv",
                    dtype={"cpf": "string",
                           "numero": "string",
                           "salario": "string"})

dados["cpf_formatado"] = (dados["cpf"]
                           .str.replace(".", "")
                           .str.replace("-", "")
                           .str.replace(" ", ""))

dados["numero_formatado"] = (dados["numero"]
                            # Remover tudo que não é número
                             .str.replace(r"\D", "", regex=True)
                             )

dados["salario_formatado"] = (dados["salario"]
                            # Limpando caracteres indesejados (Símbolos, letras e espaços)
                              .str.replace(r"[^\d,.\-]", "", regex=True)
                            # Removendo o ponto de milhar
                              .str.replace(r"\.(?=\d{3}(?:\.|,|$))", "", regex=True)
                            # (Vírgula para Ponto)
                              .str.replace(r",",".", regex=False)
                            # Convertendo para float
                              .astype(float)
                              )

print(dados)
