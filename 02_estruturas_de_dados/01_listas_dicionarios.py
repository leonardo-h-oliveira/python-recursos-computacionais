"""
Tema: Listas e dicionários em Python
Objetivo: Demonstrar como armazenar e organizar dados simples.
Autor: Leonardo Henrique Oliveira
"""

def exemplo_lista():
    notas = [70, 85, 60, 90]
    print("Notas:", notas)
    print("Primeira nota:", notas[0])
    print("Quantidade de notas:", len(notas))


def exemplo_dicionario():
    aluno = {
        "nome": "João",
        "curso": "Engenharia",
        "nota": 82
    }

    print("Aluno:", aluno)
    print("Nome:", aluno["nome"])
    print("Nota:", aluno["nota"])


if __name__ == "__main__":
    exemplo_lista()
    exemplo_dicionario()
