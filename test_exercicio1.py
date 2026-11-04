import pytest

from exercicio1 import classificar_produto


# 1. Produto sem estoque
def test_produto_sem_estoque():
    assert classificar_produto(0) == "Sem estoque"


# 2. Produto com estoque baixo
def test_produto_com_estoque_baixo():
    assert classificar_produto(3) == "Estoque baixo"


# 3. Produto com estoque normal
def test_produto_com_estoque_normal():
    assert classificar_produto(12) == "Estoque normal"


# 4. Produto com estoque alto
def test_produto_com_estoque_alto():
    assert classificar_produto(50) == "Estoque alto"


# 5. Quantidade negativa
def test_quantidade_negativa():
    assert classificar_produto(-5) == "Quantidade inválida"


# Permite rodar este arquivo direto pelo ▶ do VS Code
if __name__ == "__main__":
    resultado = pytest.main([__file__, "-v", "-p", "no:cacheprovider"])
    print("\nExercício 1:", "VALIDADO" if resultado == 0 else "NÃO VALIDADO")
