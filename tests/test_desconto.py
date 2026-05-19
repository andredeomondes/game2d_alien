import pytest
from desconto import Pedido, DescontoFixo, DescontoPercentual, DescontoApp


# --- Assert simples: DescontoNormal (DescontoFixo) ---

def test_desconto_normal():
    pedido = Pedido(100.0)
    desconto = DescontoFixo(20.0)
    app = DescontoApp(pedido, desconto)
    assert app.calcular_total_com_desconto() == 80.0


# --- Fixture: DescontoVIP (10% off) ---

@pytest.fixture
def pedido_vip():
    return Pedido(200.0)

def test_desconto_vip(pedido_vip):
    desconto = DescontoPercentual(10)
    app = DescontoApp(pedido_vip, desconto)
    assert app.calcular_total_com_desconto() == 180.0


# --- Parametrize: DescontoPremium (30% off) ---

@pytest.mark.parametrize("valor,esperado", [
    (100, 70.0),
    (200, 140.0),
    (300, 210.0),
])
def test_desconto_premium(valor, esperado):
    pedido = Pedido(valor)
    desconto = DescontoPercentual(30)
    app = DescontoApp(pedido, desconto)
    assert app.calcular_total_com_desconto() == esperado
