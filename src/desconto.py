from abc import ABC, abstractmethod


class IDesconto(ABC):
    """Classe base para todos os tipos de desconto."""

    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass


class Pedido:
    """Representa um pedido com injeção de estratégia de desconto."""

    def __init__(self, desconto: IDesconto) -> None:
        self.desconto = desconto

    def total(self, valor: float) -> float:
        return valor - self.desconto.calcular(valor)


class DescontoFixo(IDesconto):
    """Subtrai um valor fixo (ex: R$ 20,00 off)."""

    def __init__(self, valor_desconto: float) -> None:
        self.valor_desconto = valor_desconto

    def calcular(self, valor: float) -> float:
        return self.valor_desconto


class DescontoPercentual(IDesconto):
    """Subtrai uma porcentagem (ex: 10% off)."""

    def __init__(self, porcentagem: float) -> None:
        self.porcentagem = porcentagem

    def calcular(self, valor: float) -> float:
        return valor * (self.porcentagem / 100)


if __name__ == "__main__":
    meu_pedido = Pedido(DescontoPercentual(20))
    print(f"Total a pagar: R$ {meu_pedido.total(500.0)}")
