import pandas as pd

df_estoque_supermercado = pd.read_csv("estoque_supermercado.csv")

# 1. Coluna preco
df_estoque_supermercado["preco"] = (
    df_estoque_supermercado["preco"]
    .astype(str)
    .str.replace(r"R\$", "", regex=True)
    .str.strip()
    .str.replace(",", ".", regex=False)
)

df_estoque_supermercado["preco"] = (
    pd.to_numeric(df_estoque_supermercado["preco"], errors="coerce"))

# 2. Coluna quantidade
df_estoque_supermercado["quantidade"] = (
    pd.to_numeric(df_estoque_supermercado["quantidade"], errors="coerce"))

df_estoque_supermercado["quantidade"] = (
    df_estoque_supermercado["quantidade"].fillna(0).astype(int))

# 3. Coluna setor
df_estoque_supermercado["setor"] = (
    df_estoque_supermercado["setor"]
    .astype(str)
    .str.strip()
    .str.lower()
)

df_estoque_supermercado["setor"] = (
    df_estoque_supermercado["setor"]
    .replace("nan", "sem setor")
    .fillna("sem setor"))

# 4. Coluna data_compra e data_vencimento
df_estoque_supermercado["data_compra"] = pd.to_datetime(
    df_estoque_supermercado["data_compra"],
    format="%d/%m/%Y",
    errors="coerce"
)

df_estoque_supermercado["data_vencimento"] = pd.to_datetime(
    df_estoque_supermercado["data_vencimento"],
    format="%d/%m/%Y",
    errors="coerce"
)


df_estoque_supermercado.to_csv("dados_padronizados.csv", index=False)

print(df_estoque_supermercado)