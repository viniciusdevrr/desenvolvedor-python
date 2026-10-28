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

"""