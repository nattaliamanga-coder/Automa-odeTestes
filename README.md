# Automação de Testes – Python

Exercícios 1 a 6 com **Pytest** e **unittest.mock**.

| Exercício | Funções | Testes |
|---|---|---|
| 1 – Classificação de produto | `exercicio1.py` | `test_exercicio1.py` |
| 2 – Inversão de palavras | `exercicio2.py` | `test_exercicio2.py` |
| 3 – Validação de CPF simplificada | `exercicio3.py` | `test_exercicio3.py` |
| 4 – Código de identificação (Mock) | `exercicio4.py` | `test_exercicio4.py` |
| 5 – Verificação de acesso (Mock) | `exercicio5.py` | `test_exercicio5.py` |
| 6 – Fila de atendimento (Mock) | `exercicio6.py` | `test_exercicio6.py` |

## Rodar localmente

```bash
pip install -r requirements.txt
pytest -v                      # todos os exercícios
pytest test_exercicio3.py -v   # só um exercício
```

Ou abra um `test_exercicioN.py` no VS Code e clique em ▶.

## Pipeline (GitHub Actions)

O arquivo `.github/workflows/testes.yml` roda os testes a cada push.
O resultado aparece na aba **Actions** do repositório, com um passo para cada exercício.
