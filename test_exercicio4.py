from unittest.mock import patch

import pytest

from exercicio4 import criar_identificacao

# O patch aponta para onde a função é USADA: criar_identificacao procura
# gerar_codigo dentro do módulo exercicio4, então é lá que ela é substituída.
ALVO = "exercicio4.gerar_codigo"


# 1. Verificar se a mensagem foi gerada corretamente
def test_mensagem_gerada_corretamente():
    with patch(ALVO, return_value="USR-1234"):
        resultado = criar_identificacao("Carlos")
    assert resultado == "Usuário Carlos cadastrado com código USR-1234."


# 2. Verificar se gerar_codigo() foi chamada
def test_gerar_codigo_foi_chamada():
    with patch(ALVO, return_value="USR-1234") as mock_gerar:
        criar_identificacao("Carlos")
    mock_gerar.assert_called()


# 3. Verificar se a função foi chamada apenas uma vez
def test_gerar_codigo_chamada_apenas_uma_vez():
    with patch(ALVO, return_value="USR-1234") as mock_gerar:
        criar_identificacao("Carlos")
    mock_gerar.assert_called_once()


# 4. Utilizar Mock para simular diferentes códigos
@pytest.mark.parametrize("codigo", ["USR-0001", "USR-5678", "USR-9999"])
def test_simula_codigos_diferentes(codigo):
    with patch(ALVO, return_value=codigo):
        resultado = criar_identificacao("Carlos")
    assert resultado == f"Usuário Carlos cadastrado com código {codigo}."


# 5. Verificar o comportamento com nomes diferentes
@pytest.mark.parametrize(
    "nome",
    ["Carlos", "Ana", "Maria Eduarda", "João"],
    ids=["Carlos", "Ana", "Maria_Eduarda", "Joao"],
)
def test_nomes_diferentes(nome):
    with patch(ALVO, return_value="USR-1234"):
        resultado = criar_identificacao(nome)
    assert resultado == f"Usuário {nome} cadastrado com código USR-1234."


# Permite rodar este arquivo direto pelo ▶ do VS Code
if __name__ == "__main__":
    resultado = pytest.main([__file__, "-v", "-p", "no:cacheprovider"])
    print("\nExercício 4:", "VALIDADO" if resultado == 0 else "NÃO VALIDADO")
