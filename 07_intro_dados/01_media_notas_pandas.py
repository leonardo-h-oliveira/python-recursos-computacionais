"""
Tema: Introdução ao Pandas
Objetivo: Calcular a média de notas utilizando estrutura de dados tabular.
Autor: Leonardo Henrique Oliveira
"""

import pandas as pd

def calcula_media_dataframe(notas):
    df = pd.DataFrame(notas, columns=["nota"])
    media = df["nota"].mean()
    return media


if __name__ == "__main__":
    notas = [70, 85, 60, 90]
    media = calcula_media_dataframe(notas)

    print("Notas:", notas)
    print("Média (Pandas):", media)
