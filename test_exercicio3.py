import pytest

from exercicio3 import validar_documento


# 1. Documento com 11 dígitos
def test_documento_com_11_digitos():
    assert validar_documento("12345678900") is True


# 2. Documento formatado
def test_documento_formatado():
    assert validar_documento("123.456.789-00") is True


# 3. Documento com menos de 11 dígitos
def test_documento_com_menos_de_11_digitos():
    assert validar_documento("1234567890") is False


# 4. Documento com mais de 11 dígitos
def test_documento_com_mais_de_11_digitos():
    assert validar_documento("123456789000") is False


# 5. Documento contendo letras
def test_documento_com_letras():
    assert validar_documento("123.456.78A-00") is False


# 6. Documento vazio
def test_documento_vazio():
    assert validar_documento("") is False


# Permite rodar este arquivo direto pelo ▶ do VS Code
if __name__ == "__main__":
    resultado = pytest.main([__file__, "-v", "-p", "no:cacheprovider"])
    print("\nExercício 3:", "VALIDADO" if resultado == 0 else "NÃO VALIDADO")
