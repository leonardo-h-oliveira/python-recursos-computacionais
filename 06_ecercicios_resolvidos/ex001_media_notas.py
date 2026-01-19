"""
Exercício 01 – Cálculo da média de notas
Objetivo: Calcular a média de uma lista de notas e informar a situação do aluno.
Autor: Leonardo Henrique Oliveira
"""

def calcula_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media


def situacao_aluno(media):
    if media >= 60:
        return "Aprovado"
    else:
        return "Reprovado"


if __name__ == "__main__":
    notas = [70, 85, 60, 90]
    media = calcula_media(notas)

    print("Notas:", notas)
    print("Média:", media)
    print("Situação:", situacao_aluno(media))
