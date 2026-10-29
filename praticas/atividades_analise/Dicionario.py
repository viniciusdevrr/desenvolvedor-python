"""
pd.to_numeric()	Transforma texto em número (inteiro ou decimal).
• errors='coerce' = Transforma textos inválidos em NaN.
• arg = A coluna a converter.
• errors='raise' = Dá erro se achar texto (padrão).

.str.replace()	Procura um pedaço de texto e troca por outro.
• pat = O texto/símbolo que você quer tirar/mudar.
• repl = O texto que vai entrar no lugar.
• regex=False (ou True) = Se vai usar padrões avançados ou texto comum.

.str.strip() Remove espaços vazios do início e do fim do texto.
• (Geralmente usado vazio) para limpar espaços acidentais nas pontas.

.fillna()	Substitui os valores nulos (NaN) por outra coisa.
• value = O valor fixo ou cálculo que vai preencher o vazio (ex: 0, ou .mean()).

.astype()	Força a coluna inteira a mudar para um tipo de dado.
• dtype = O tipo desejado:
- 'int' (inteiro)
- 'float' (decimal)
- 'str' (texto)

1. .describe()
O que faz: Gera um resumo estatístico das colunas numéricas
(média, mínimo, máximo, quartis).

O que usar: df.describe() (padrão numérico) ou df.describe(include='all')
(inclui colunas de texto). Ideal para achar erros grosseiros nos dados.

2. .info()
O que faz: Mostra a estrutura do DataFrame
(total de linhas, colunas, quantidade de dados preenchidos e tipos de dados).

O que usar: df.info(). Excelente para conferir se as conversões de tipo
(int, float, datetime) funcionaram corretamente.

3. .str.fullmatch()
O que faz: Verifica se um texto inteiro corresponde exatamente a um padrão (Regex),
retornando True ou False.

O que usar: df["coluna"].str.fullmatch(r"padrão"). Útil para validar formatos exatos
(ex: CPFs, CEPs ou códigos específicos). Diferente do .str.contains,
que busca apenas em pedaços do texto..

"""