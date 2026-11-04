"""Exercício 6 – Sistema de fila de atendimento."""

from collections import deque

# Fila e registro fictícios (nos testes as funções são substituídas por Mock).
fila_clientes = deque(["Ana", "Bruno", "Carla"])
atendimentos_registrados = []


def obter_proximo_cliente():
    """Retira e retorna o próximo cliente da fila, ou None se ela estiver vazia."""
    if fila_clientes:
        return fila_clientes.popleft()
    return None


def registrar_atendimento(cliente):
    """Simula o registro do atendimento. Retorna True quando registrado."""
    atendimentos_registrados.append(cliente)
    return True


def atender_proximo_cliente():
    """Atende o próximo cliente da fila e informa o resultado."""
    cliente = obter_proximo_cliente()

    if not cliente:
        return "Fila vazia"

    if registrar_atendimento(cliente):
        return "Atendimento realizado"
    return "Falha no atendimento"
