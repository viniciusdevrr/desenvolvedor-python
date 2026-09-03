print("Questão 6: O Erro de Verificação (Análise e Correção de Código) \n")

senha_cadastrada = 1234
senha_digitada = input("Digite sua senha: ")
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)

"""
Isso acontece devido à diferença entre os tipos de dados no Python

A variável senha_cadastrada = 1234 foi armazenada como um número inteiro.
A função input() sempre retorna o valor digitado como um texto (str ou string), mesmo que o usuário digite apenas 
números.

"""

# A senha cadastrada pode ser mantida como inteiro ou texto.
# Vamos converter a entrada do usuário para o mesmo tipo da senha cadastrada.
senha_cadastrada = 1234
# Convertemos o resultado do input() de string para inteiro usando int()
senha_digitada = int(input("Digite sua senha: "))
# Agora ambos são inteiros (int), permitindo uma comparação correta
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)