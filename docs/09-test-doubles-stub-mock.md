# Commit 9 — Test Doubles: Stub, Mock e Coverage

**Branch:** `feature/tests_units`  
**Arquivos:** `tests/doubles.py`, `tests/test_doubles.py`, `tests/test_game_alien.py`

## O que são Test Doubles

Objetos falsos que substituem dependências reais nos testes. Permitem testar uma classe de forma isolada, sem depender de banco, rede, pygame, ou outras classes complexas.

## Stub

> Simula uma dependência retornando respostas controladas.

**Foco:** controlar o que a dependência retorna.  
**Não verifica:** se foi chamada, quantas vezes, com quais argumentos.

```python
# tests/doubles.py
class StubSemDesconto(IDesconto):
    def calcular(self, valor: float) -> float:
        return 0  # sempre retorna zero — nenhum desconto

# tests/test_doubles.py
def test_pedido_com_stub():
    pedido = Pedido(StubSemDesconto())
    assert pedido.total(100) == 100  # 100 - 0 = 100
```

**Pergunta respondida:** "O `Pedido` calcula corretamente independente de quem faz o desconto?"

## Mock

> Substitui uma dependência E verifica como ela foi usada.

**Foco:** verificar interação — se foi chamada, quantas vezes, com quais argumentos.

```python
def test_pedido_com_mock_desconto(mocker):
    mock_desconto = mocker.Mock()
    mock_desconto.calcular.return_value = 10  # define o retorno

    pedido = Pedido(mock_desconto)
    resultado = pedido.total(100)

    assert resultado == 90                              # verifica resultado
    mock_desconto.calcular.assert_called()              # foi chamada?
    mock_desconto.calcular.assert_called_once_with(100) # com argumento 100?
    assert mock_desconto.calcular.call_count == 1       # exatamente uma vez?
```

## Aplicação no jogo — `test_game_alien.py`

### Stub de Settings

```python
class StubSettings:
    ship_limit = 3
    alien_points = 50
```

Isola `GameStats` do `Settings` real (que depende de outros arquivos do jogo). O stub retorna valores fixos e controláveis.

```python
def test_game_stats_estado_inicial():
    stats = GameStats(StubSettings())
    assert stats.score == 0
    assert stats.ships_left == 3
    assert stats.game_active is True
```

### Mock de método

```python
def test_game_stats_reset_com_mock(mocker):
    stats = GameStats(StubSettings())
    stats.score = 500
    stats.ships_left = 0

    mock_reset = mocker.patch.object(stats, "reset_stats", wraps=stats.reset_stats)
    stats.reset_stats()

    mock_reset.assert_called_once()   # verifica que reset foi chamado
    assert stats.score == 0           # e que realmente zerou
    assert stats.ships_left == 3
```

`wraps=stats.reset_stats` mantém o comportamento real mas espiona a chamada.

## Stub vs Mock — quando usar cada um

| | Stub | Mock |
|---|---|---|
| Objetivo | Controlar retorno | Verificar interação |
| Verifica chamadas | Não | Sim |
| Uso típico | Isolar dependência | Garantir que método foi chamado |

## Relatório HTML

```bash
pytest --html=relatorio.html
```

Gera arquivo visual com resultado de cada teste, duração e detalhes de falhas.

## Coverage

```bash
coverage run -m pytest   # roda testes medindo cobertura
coverage report          # exibe % de linhas executadas por arquivo
```

Resultado do projeto:

```
src/desconto.py     87%
src/game_stats.py  100%
tests/doubles.py   100%
TOTAL               97%
```

`htmlcov/` e `relatorio.html` estão no `.gitignore` — não sobem para o repositório.
