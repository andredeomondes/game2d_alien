# Commit 2 — Análise estática com Ruff e mypy

**Branch:** `feature/analise-estatica`  
**Mensagem:** `Aplica análise estática com ruff e mypy --strict`

## O que foi feito

Aplicação de ferramentas de análise estática para garantir qualidade de código sem precisar executar o programa.

## Ferramentas utilizadas

### Ruff

Verificador de estilo e qualidade para Python (substitui flake8, isort, pycodestyle).

```bash
ruff check .        # verifica problemas
ruff check . --fix  # corrige automaticamente
ruff format .       # formata o código (como o Black)
```

**O que o ruff corrigiu:**
- Adicionou linha em branco entre imports e classe
- Corrigiu aspas simples para duplas
- Ajustou espaçamento em comentários inline (`# texto` → `  # texto`)
- Adicionou newline no final do arquivo

### mypy

Verificador de tipos estáticos. Analisa se os tipos no código são coerentes.

```bash
mypy .          # verificação padrão
mypy --strict . # verificação rigorosa — exige type hints em tudo
```

**Erros encontrados pelo `mypy --strict`:**

```
error: Function is missing a return type annotation  [no-untyped-def]
```

## O que foi corrigido

Adicionados **type hints** nos métodos da classe:

```python
# Antes
def __init__(self):
def run_game(self):

# Depois
def __init__(self) -> None:
def run_game(self) -> None:
```

## Por que isso importa

Type hints não mudam como o programa executa, mas:
- Deixam o código mais legível
- Permitem que ferramentas detectem erros de tipo antes de rodar
- São obrigatórios em código profissional com `mypy --strict`
