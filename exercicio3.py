"""Exercício 3 – Validação de CPF simplificada (sem dígitos verificadores)."""

import re


def validar_documento(documento):
    """Retorna True se o documento tiver exatamente 11 dígitos numéricos.

    Pontos e hífen são removidos antes da validação, então
    "123.456.789-00" é aceito.
    """
    if not isinstance(documento, str):
        return False

    limpo = documento.replace(".", "").replace("-", "")

    # [0-9] em vez de \d para aceitar só os dígitos de 0 a 9.
    return re.fullmatch(r"[0-9]{11}", limpo) is not None
