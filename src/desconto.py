from abc import ABC, abstractmethod


class Pedido:
    """Representa um pedido com um valor total."""

    def __init__(self, valor: float) -> None:
        self.valor = valor

    def get_valor(self) -> float:
        return self.valor


class Desconto(ABC):
    """Classe base para todos os tipos de desconto."""

    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass


class DescontoFixo(Desconto):
    """Subtrai um valor fixo (ex: R$ 20,00 off)."""

    def __init__(self, valor_desconto: float) -> None:
        self.valor_desconto = valor_desconto

    def calcular(self, valor: float) -> float:
        return valor - self.valor_desconto


class DescontoPercentual(Desconto):
    """Subtrai uma porcentagem (ex: 10% off)."""

    def __init__(self, porcentagem: float) -> None:
        self.porcentagem = porcentagem

    def calcular(self, valor: float) -> float:
        return valor * (1 - self.porcentagem / 100)


class DescontoApp:
    """Orquestra a aplicação do desconto sobre o pedido."""

    def __init__(self, pedido: Pedido, desconto_estrategia: Desconto) -> None:
        self.pedido = pedido
        self.desconto_estrategia = desconto_estrategia

    def calcular_total_com_desconto(self) -> float:
        valor_original = self.pedido.get_valor()
        return self.desconto_estrategia.calcular(valor_original)


if __name__ == "__main__":
    meu_pedido = Pedido(500.0)
    meu_desconto = DescontoPercentual(20)

    app = DescontoApp(meu_pedido, meu_desconto)
    print(f"Total a pagar: R$ {app.calcular_total_com_desconto()}")
