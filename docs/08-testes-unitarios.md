# Commit 8 — Testes Unitários com pytest

**Branch:** `feature/tests_units`  
**Arquivo:** `tests/test_desconto.py`

## O que são testes unitários

Verificam uma unidade isolada de código (função, método, classe) sem depender de sistemas externos. O objetivo é garantir que cada peça funciona corretamente por si só.

## Os 3 elementos principais

### 1. Assert (verificação direta)

```python
def test_desconto_normal():
    pedido = Pedido(DescontoFixo(20.0))
    assert pedido.total(100.0) == 80.0
```

`assert` verifica se a condição é verdadeira. Se falhar, o teste falha com mensagem clara.

### 2. Fixture (dados reutilizáveis)

```python
@pytest.fixture
def pedido_vip():
    return Pedido(DescontoPercentual(10))

def test_desconto_vip(pedido_vip):
    assert pedido_vip.total(200.0) == 180.0
```

Fixture cria o objeto uma vez e injeta em qualquer teste que precisar. Evita repetição de setup. O pytest detecta que `pedido_vip` é fixture pelo nome do parâmetro.

### 3. Parametrize (múltiplos cenários)

```python
@pytest.mark.parametrize("valor,esperado", [
    (100, 70.0),
    (200, 140.0),
    (300, 210.0),
])
def test_desconto_premium(valor, esperado):
    pedido = Pedido(DescontoPercentual(30))
    assert pedido.total(valor) == esperado
```

Um único teste roda com N conjuntos de dados. Cada linha gera um caso independente no relatório. Aqui testa 30% de desconto em 3 valores diferentes.

## Executando

```bash
pytest       # executa todos os testes
pytest -v    # modo verboso (mostra nome de cada teste)
```

## pytest.ini

```ini
[pytest]
testpaths = tests
pythonpath = src tests
```

- `testpaths`: onde o pytest procura testes
- `pythonpath`: pastas adicionadas ao `sys.path` para que os imports funcionem
