# Commit 7 — Strategy Pattern com Descontos

**Branch:** `feature/applying-solid`  
**Mensagem:** `feat: adiciona exemplo de Strategy Pattern com descontos`  
**Correção:** `fix: corrige desconto.py para estrutura coerente com spec`

## O que é Strategy Pattern

> "Defina uma família de algoritmos, encapsule cada um deles e torne-os intercambiáveis."

Permite trocar o comportamento de um objeto em tempo de execução sem modificar o objeto em si. É uma aplicação direta do OCP.

## Estrutura do `desconto.py`

```
IDesconto (ABC)
├── DescontoFixo       → subtrai valor fixo
└── DescontoPercentual → subtrai porcentagem

Pedido(desconto: IDesconto)
└── total(valor) → valor - desconto.calcular(valor)
```

## Por que `IDesconto` e não `Desconto`

O prefixo `I` é convenção para **Interface** — indica que a classe é um contrato que outras devem cumprir. `IDesconto` não faz cálculo; define apenas que qualquer desconto precisa ter `calcular(valor)`.

## Diferença entre as versões

| | Versão anterior | Versão corrigida |
|---|---|---|
| `Pedido` | `Pedido(valor_total)` | `Pedido(desconto)` |
| `calcular` | recebe `Pedido` | recebe `float` |
| `DescontoFixo.calcular` | retorna total após desconto | retorna só o valor do desconto |
| Orquestrador | `DescontoApp` | `Pedido.total(valor)` |

## Como trocar o algoritmo em tempo de execução

```python
pedido = Pedido(DescontoFixo(20))
print(pedido.total(100))   # 80.0

pedido.desconto = DescontoPercentual(10)
print(pedido.total(100))   # 90.0
```

Nenhuma classe foi modificada — só a estratégia injetada.
