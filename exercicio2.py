"""Exercício 2 – Inversão de palavras."""


def inverter_palavras(texto):
    """Retorna a frase com a ordem das palavras invertida.

    split() sem argumento já descarta espaços extras (no início, no fim e
    repetidos entre palavras), e uma string vazia vira lista vazia, que o
    join transforma de volta em "".
    """
    palavras = texto.split()
    return " ".join(reversed(palavras))
