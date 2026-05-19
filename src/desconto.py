from abc import ABC, abstractmethod


class Pedido:
    """Representa um pedido com um valor total."""

    def __init__(self, valor_total: float) -> None:
        self.valor_total = valor_total

    def get_valor_total(self) -> float:
        return self.valor_total


class Desconto(ABC):
    """Interface para diferentes estratégias de desconto."""

    @abstractmethod
    def calcular(self, pedido: Pedido) -> float:
        pass


class DescontoFixo(Desconto):
    """Aplica um desconto de valor fixo (ex: R$ 10,00)."""

    def __init__(self, valor_desconto: float) -> None:
        self.valor_desconto = valor_desconto

    def calcular(self, pedido: Pedido) -> float:
        return self.valor_desconto


class DescontoPercentual(Desconto):
    """Aplica um desconto baseado em porcentagem (ex: 10%)."""

    def __init__(self, porcentagem: float) -> None:
        self.porcentagem = porcentagem

    def calcular(self, pedido: Pedido) -> float:
        return pedido.valor_total * (self.porcentagem / 100)


class DescontoApp:
    """Classe que executa a aplicação do desconto no pedido."""

    def __init__(self, pedido: Pedido, estrategia_desconto: Desconto) -> None:
        self.pedido = pedido
        self.estrategia_desconto = estrategia_desconto

    def calcular_valor_final(self) -> float:
        valor_desconto = self.estrategia_desconto.calcular(self.pedido)
        valor_final = self.pedido.valor_total - valor_desconto
        return max(0, valor_final)


if __name__ == "__main__":
    meu_pedido = Pedido(100.0)

    regra_15 = DescontoPercentual(15)

    app = DescontoApp(meu_pedido, regra_15)
    print(f"Valor Final com Desconto: R$ {app.calcular_valor_final()}")
