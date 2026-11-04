"""Exercício 1 – Classificação de produto no estoque."""


def classificar_produto(quantidade):
    """Classifica a situação de um produto de acordo com a quantidade em estoque."""
    if quantidade < 0:
        return "Quantidade inválida"
    if quantidade == 0:
        return "Sem estoque"
    if quantidade <= 5:
        return "Estoque baixo"
    if quantidade <= 20:
        return "Estoque normal"
    return "Estoque alto"
