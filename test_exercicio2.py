import pytest

from exercicio2 import inverter_palavras


# 1. Frase com várias palavras
def test_frase_com_varias_palavras():
    assert inverter_palavras("Python é muito interessante") == "interessante muito é Python"


# 2. Frase com apenas uma palavra
def test_frase_com_uma_palavra():
    assert inverter_palavras("Python") == "Python"


# 3. Frase vazia
def test_frase_vazia():
    assert inverter_palavras("") == ""


# 4. Frase com espaços extras
def test_frase_com_espacos_extras():
    assert inverter_palavras("  Python   é    legal  ") == "legal é Python"


# 5. Frase com números e letras
def test_frase_com_numeros_e_letras():
    assert inverter_palavras("Tenho 2 gatos e 3 cães") == "cães 3 e gatos 2 Tenho"


# Permite rodar este arquivo direto pelo ▶ do VS Code
if __name__ == "__main__":
    resultado = pytest.main([__file__, "-v", "-p", "no:cacheprovider"])
    print("\nExercício 2:", "VALIDADO" if resultado == 0 else "NÃO VALIDADO")
