print("Questão 5: Sistema de Cálculo de Idade \n");

ano_nascimento = int(input("Digite o ano de nascimento: "));
ano_atual = int(input("Digite o ano atual: "));

idade_usuario = ano_atual - ano_nascimento;

print("O usuário tem", idade_usuario, "anos de idade.");