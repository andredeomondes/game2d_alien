from desconto import IDesconto


class StubSemDesconto(IDesconto):
    """Stub que simula ausência de desconto — sempre retorna 0."""

    def calcular(self, valor: float) -> float:
        return 0
