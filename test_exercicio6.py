from unittest.mock import patch

import pytest

from exercicio6 import atender_proximo_cliente

ALVO_OBTER = "exercicio6.obter_proximo_cliente"
ALVO_REGISTRAR = "exercicio6.registrar_atendimento"


# 1. Atendimento realizado com sucesso
def test_atendimento_realizado_com_sucesso():
    with patch(ALVO_OBTER, return_value="Ana"), \
         patch(ALVO_REGISTRAR, return_value=True):
        assert atender_proximo_cliente() == "Atendimento realizado"


# 2. Fila vazia
def test_fila_vazia():
    with patch(ALVO_OBTER, return_value=None), \
         patch(ALVO_REGISTRAR):
        assert atender_proximo_cliente() == "Fila vazia"


# 3. Falha ao registrar atendimento
def test_falha_ao_registrar_atendimento():
    with patch(ALVO_OBTER, return_value="Ana"), \
         patch(ALVO_REGISTRAR, return_value=False):
        assert atender_proximo_cliente() == "Falha no atendimento"


# 4. Verificar se obter_proximo_cliente() foi chamada
def test_obter_proximo_cliente_foi_chamada():
    with patch(ALVO_OBTER, return_value="Ana") as mock_obter, \
         patch(ALVO_REGISTRAR, return_value=True):
        atender_proximo_cliente()
    mock_obter.assert_called_once()


# 5. Verificar se registrar_atendimento() foi chamada com o cliente correto
def test_registrar_chamada_com_cliente_correto():
    with patch(ALVO_OBTER, return_value="Bruno"), \
         patch(ALVO_REGISTRAR, return_value=True) as mock_registrar:
        atender_proximo_cliente()
    mock_registrar.assert_called_once_with("Bruno")


# 6. Verificar se registrar_atendimento() NÃO foi chamada com a fila vazia
def test_registrar_nao_chamada_com_fila_vazia():
    with patch(ALVO_OBTER, return_value=None), \
         patch(ALVO_REGISTRAR) as mock_registrar:
        atender_proximo_cliente()
    mock_registrar.assert_not_called()


# Permite rodar este arquivo direto pelo ▶ do VS Code
if __name__ == "__main__":
    resultado = pytest.main([__file__, "-v", "-p", "no:cacheprovider"])
    print("\nExercício 6:", "VALIDADO" if resultado == 0 else "NÃO VALIDADO")
