import pytest
from desconto import Pedido, DescontoFixo, DescontoPercentual


# --- Assert simples: DescontoNormal (DescontoFixo) ---

def test_desconto_normal():
    pedido = Pedido(DescontoFixo(20.0))
    assert pedido.total(100.0) == 80.0


# --- Fixture: DescontoVIP (10% off) ---

@pytest.fixture
def pedido_vip():
    return Pedido(DescontoPercentual(10))

def test_desconto_vip(pedido_vip):
    assert pedido_vip.total(200.0) == 180.0


# --- Parametrize: DescontoPremium (30% off) ---

@pytest.mark.parametrize("valor,esperado", [
    (100, 70.0),
    (200, 140.0),
    (300, 210.0),
])
def test_desconto_premium(valor, esperado):
    pedido = Pedido(DescontoPercentual(30))
    assert pedido.total(valor) == esperado
