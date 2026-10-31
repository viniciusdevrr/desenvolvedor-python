import pandas as pd

df_estoque_supermercado = pd.read_csv("estoque_supermercado.csv")

# Coluna preco
df_estoque_supermercado["preco"] = (
    df_estoque_supermercado["preco"]
    .astype(str)
    .str.replace(r"[^\d,.\-]", "", regex=True)
    .str.strip()
    .str.replace(",", ".", regex=False)
)
df_estoque_supermercado["preco"] = pd.to_numeric(df_estoque_supermercado["preco"], errors="coerce")

# Coluna quantidade
df_estoque_supermercado["quantidade"] = pd.to_numeric(df_estoque_supermercado["quantidade"], errors="coerce")
df_estoque_supermercado["quantidade"] = df_estoque_supermercado["quantidade"].fillna(0).astype(int)

# Coluna setor
df_estoque_supermercado["setor"] = (
    df_estoque_supermercado["setor"]
    .astype(str)
    .str.strip()
    .str.lower()
)
df_estoque_supermercado["setor"] = (
    df_estoque_supermercado["setor"]
    .replace("nan", "sem setor")
    .fillna("sem setor")
)

# Coluna de Datas
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

# for index, linha in df_estoque_supermercado.iterrows():
#
#     if pd.isna(df_estoque_supermercado.at[index, "preco"]):
#         while True:
#             print(f'\nO produto {df_estoque_supermercado.at[index, "nome"]} está sem PRECO.')
#             try:
#                 novo_preco = input("Digite o preco do produto: ")
#                 df_estoque_supermercado.at[index, "preco"] = float(novo_preco)
#                 break
#             except ValueError:
#                 print("Digite um preco válido usando números!")
#
#     if df_estoque_supermercado.at[index, "quantidade"] == 0:
#         while True:
#             print(f"\nNão foi cadastrado a quantidade de estoque do produto {df_estoque_supermercado.at[index, "nome"]}.")
#             opcao = input("Para adicionar digite [sim]\n"
#                           "Para manter sem estoque digite [nao]\n= ")
#             if opcao.lower() == 'sim':
#                 try:
#                     nova_qtd = int(input(f"Digite a quantidade de {df_estoque_supermercado.at[index, "nome"]}: "))
#                     df_estoque_supermercado.at[index, "quantidade"] = nova_qtd
#                     break
#                 except ValueError:
#                     print("Digite um número inteiro válido!")
#             elif opcao.lower() == 'nao':
#                 print(f"O produto {df_estoque_supermercado.at[index, "nome"]} manteve estoque zerado.")
#                 break
#             else:
#                 print("Digite apenas [sim] ou [nao]!")
#
#     if pd.isna(df_estoque_supermercado.at[index, "data_compra"]):
#         while True:
#             print(f"\nNo index {index} o produto {df_estoque_supermercado.at[index, "nome"]} está sem DATA DE COMPRA.")
#             nova_data = input("Digite a data de COMPRA no formato DD/MM/AAAA (ex: 24/10/2026): ")
#             try:
#                 data_convertida = pd.to_datetime(nova_data, format="%d/%m/%Y")
#                 df_estoque_supermercado.at[index, "data_compra"] = data_convertida
#                 break
#             except ValueError:
#                 print("Data inválida ou fora do padrão DD/MM/AAAA! Tente novamente.")
#
#     if pd.isna(df_estoque_supermercado.at[index, "data_vencimento"]):
#         while True:
#             print(
#                 f"\nNo index {index} o produto {df_estoque_supermercado.at[index, "nome"]} está sem DATA DE VENCIMENTO.")
#             nova_data = input("Digite a data de VENCIMENTO no formato DD/MM/AAAA (ex: 31/10/2026): ")
#             try:
#                 data_convertida = pd.to_datetime(nova_data, format="%d/%m/%Y")
#                 df_estoque_supermercado.at[index, "data_vencimento"] = data_convertida
#                 break
#             except ValueError:
#                 print("Data inválida ou fora do padrão DD/MM/AAAA! Digite novamente.")

#crianco coluna valor_total_estoque
df_estoque_supermercado["valor_total_estoque"] = (
        df_estoque_supermercado["quantidade"] * df_estoque_supermercado["preco"]
)

df_estoque_supermercado.to_csv("estoque_supermercado_FINAL.csv", index=False)

print(df_estoque_supermercado)

# 1. Alerta de Vencimento
print("\n Produtos que estao VENCENDO!")
produtos_vencimento = (
        (df_estoque_supermercado["data_vencimento"] >= "2026-10-27") &
        (df_estoque_supermercado["data_vencimento"] <= "2026-11-03")
)
produtos_vencendo_semana = df_estoque_supermercado[produtos_vencimento]
print(produtos_vencendo_semana[["nome", "quantidade", "data_vencimento", "setor"]])


print("\nProduto com mais ESTOQUE em VENCIMENTO")
linha = produtos_vencendo_semana.iloc[0]
maior_nome = linha["nome"]
maior_qtd = linha["quantidade"]
maior_vencimento = linha["data_vencimento"]

for index, linha in produtos_vencendo_semana.iterrows():
    if linha["quantidade"] > maior_qtd:
        maior_qtd = linha["quantidade"]
        maior_nome = linha["nome"]
        maior_vencimento = linha["data_vencimento"]
print(f"Produto: {maior_nome} | Quantidade: {maior_qtd} | Vencimento: {maior_vencimento}")


print("\nProdutos comprados RECENTEMENTE")
compras_recentes = (
        (df_estoque_supermercado["data_compra"] >= "2026-10-24") &
        (df_estoque_supermercado["data_compra"] <= "2026-10-27")
)
produtos_recentes = df_estoque_supermercado[compras_recentes]
print(produtos_recentes[["nome", "data_compra", "quantidade"]])


print("\nProdutos sem data de VENCIMENTO")
produtos_sem_vencimento = df_estoque_supermercado[df_estoque_supermercado["data_vencimento"].isna()]
print(produtos_sem_vencimento[["nome", "setor"]])


print("\n--- Maior VALOR FINANCEIRO total por SETOR ---")
valor_por_setor = df_estoque_supermercado.groupby("setor")["valor_total_estoque"].sum()
print(valor_por_setor)

for setor, valor in valor_por_setor.items():
    if valor > valor_por_setor[setor]:
        print(f"{setor}: {valor}")

# maior_setor = ""
# maior_valor = 0
#
# for setor, valor in valor_por_setor.items():
#     if valor > maior_valor:
#         maior_valor = valor
#         maior_setor = setor
#
# print(f"\nO setor com maior valor financeiro total é '{maior_setor}' com R$ {maior_valor:.2f}.")
