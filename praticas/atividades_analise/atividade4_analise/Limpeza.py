import pandas as pd

df_estoque_supermercado = pd.read_csv("estoque_supermercado.csv")

# Coluna preco
dados_preco_formatado = (df_estoque_supermercado["preco"]
    .str.replace(r"R$", "", regex=False)
    .str.strip()
    .str.replace(",", ".", regex=False)
)
dados_preco_formatado = pd.to_numeric(dados_preco_formatado, errors="coerce")

# Coluna quantidade
dados_quantidade_formatado = pd.to_numeric(df_estoque_supermercado["quantidade"], errors="coerce")
dados_quantidade_formatado = dados_quantidade_formatado.fillna(0).astype(int)

# Coluna setor
dados_setor_formatado = (df_estoque_supermercado["setor"]
    .str.strip() # .str.Lstrip() .str.Rstrip()
    .str.lower()
)
dados_setor_formatado = dados_setor_formatado.fillna("sem setor")

