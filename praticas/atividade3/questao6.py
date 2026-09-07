print("Questão 6: O Erro de Verificação (Análise e Correção de Código) \n")

senha_cadastrada = 1234
senha_digitada = input("Digite sua senha: ")
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)

"""
Isso acontece devido à diferença entre os tipos de dados no Python

A variável senha_cadastrada = 1234 foi armazenada como um número inteiro.
A função input() sempre retorna o valor digitado como um texto (string), mesmo que o usuário digite apenas 
números.
Por isso devemos colocar a função int (inteiro) antes do input " int(input()). Depois disso quando o usuario digitar um numero
ele sera alterado para inteiro, e assim nao tera o erro da senha incorreta.

"""
print("\n")
print("Codigo Corrigido")

senha_cadastrada = 1234
senha_digitada = int(input("Digite sua senha: "))
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)