from unittest.mock import patch

import pytest

from exercicio5 import acessar_sistema

ALVO = "exercicio5.verificar_permissao"


# 1. Usuário com permissão
def test_usuario_com_permissao():
    with patch(ALVO, return_value=True):
        assert acessar_sistema("Carlos") == "Acesso autorizado"


# 2. Usuário sem permissão
def test_usuario_sem_permissao():
    with patch(ALVO, return_value=False):
        assert acessar_sistema("Visitante") == "Acesso negado"


# 3. Verificar se verificar_permissao() foi chamada
def test_verificar_permissao_foi_chamada():
    with patch(ALVO, return_value=True) as mock_verificar:
        acessar_sistema("Carlos")
    mock_verificar.assert_called_once()


# 4. Verificar se foi chamada com o usuário correto
def test_chamada_com_usuario_correto():
    with patch(ALVO, return_value=True) as mock_verificar:
        acessar_sistema("Carlos")
    mock_verificar.assert_called_once_with("Carlos")


# 5. Utilizar Mock para simular os dois cenários
@pytest.mark.parametrize(
    "tem_permissao, esperado",
    [(True, "Acesso autorizado"), (False, "Acesso negado")],
    ids=["com_permissao", "sem_permissao"],
)
def test_simula_os_dois_cenarios(tem_permissao, esperado):
    with patch(ALVO, return_value=tem_permissao) as mock_verificar:
        resultado = acessar_sistema("Ana")
    assert resultado == esperado
    mock_verificar.assert_called_once_with("Ana")


# Permite rodar este arquivo direto pelo ▶ do VS Code
if __name__ == "__main__":
    resultado = pytest.main([__file__, "-v", "-p", "no:cacheprovider"])
    print("\nExercício 5:", "VALIDADO" if resultado == 0 else "NÃO VALIDADO")
