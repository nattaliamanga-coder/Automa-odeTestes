"""Exercício 4 – Geração de código de identificação."""

import random


def gerar_codigo():
    """Gera um código fictício no formato USR-XXXX (4 dígitos aleatórios)."""
    return f"USR-{random.randint(1000, 9999)}"


def criar_identificacao(nome):
    """Cria a mensagem de cadastro usando o código gerado por gerar_codigo()."""
    codigo = gerar_codigo()
    return f"Usuário {nome} cadastrado com código {codigo}."
