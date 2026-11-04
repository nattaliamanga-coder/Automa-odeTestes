"""Exercício 5 – Verificação de acesso."""

# Lista fictícia de usuários autorizados (nos testes ela é substituída por Mock).
USUARIOS_COM_PERMISSAO = {"Carlos", "Ana", "admin"}


def verificar_permissao(usuario):
    """Retorna True se o usuário tiver permissão, False caso contrário."""
    return usuario in USUARIOS_COM_PERMISSAO


def acessar_sistema(usuario):
    """Libera ou nega o acesso com base em verificar_permissao()."""
    if verificar_permissao(usuario):
        return "Acesso autorizado"
    return "Acesso negado"
