"""
Tema: Estruturas condicionais (if / else)
Objetivo: Demonstrar tomada de decisão em Python.
Autor: Leonardo Henrique Oliveira
"""

def verifica_aprovacao(nota):
    if nota >= 60:
        return "Aprovado"
    else:
        return "Reprovado"


def verifica_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"


# Este bloco só roda quando o arquivo é executado diretamente
if __name__ == "__main__":
    print(verifica_aprovacao(75))
    print(verifica_aprovacao(40))

    print(verifica_idade(20))
    print(verifica_idade(15))
