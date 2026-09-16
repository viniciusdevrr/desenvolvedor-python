"""Crie uma única função que receba como parâmetro o nome de um aluno, 
sua nota do primeiro, segundo, terceiro e quarto bimestre.

Sua função deve calcular 
a média final desse aluno, e imprimir na tela todos os valores, 
e informar se o aluno foi reprovado ou aprovado pela média final.
"""

def calcular_media(nome, nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    print(f"Aluno: {nome} \nNotas: {nota1}, {nota2}, {nota3}, {nota4} \nMédia: {media:.2f} \nResultado: {resultado}")

calcular_media("Vinicius", 10,9,9,10)