# Commit 6 — Refatoração aplicando OCP

**Branch:** `feature/applying-solid`  
**Mensagem:** `refactor: aplicando princípio O`

## O que é OCP (Open/Closed Principle)

> "Uma classe deve estar aberta para extensão, mas fechada para modificação."

É o **O** do SOLID. Você deve conseguir **adicionar comportamento novo** sem precisar **alterar código existente**.

## Problema antes

Para criar um alienígena mais rápido, você teria que modificar `FleetManager` ou `Alien` — alterando código que já funcionava.

## O que foi feito

### 1. `fast_alien.py` — FastAlien

Novo tipo de alienígena criado por **herança**. Herda tudo de `Alien` e só sobrescreve o movimento:

```python
class FastAlien(Alien):
    def update(self) -> None:
        self.x += (self.settings.alien_speed * 2) * self.settings.fleet_direction
        self.rect.x = self.x
```

- `Alien` não foi modificado — continua igual
- `FastAlien` **estende** o comportamento multiplicando a velocidade por 2

### 2. `fleet_manager.py` — Injeção de dependência

`FleetManager` passou a aceitar a **classe do alien** como parâmetro:

```python
# Antes — acoplado ao Alien
class FleetManager:
    def __init__(self, screen, settings, ship) -> None:
        ...
    def _create_alien(self, ...):
        alien = Alien(self.screen, self.settings)  # hardcoded

# Depois — aberto para extensão
class FleetManager:
    def __init__(self, screen, settings, ship, alien_class=Alien) -> None:
        self.alien_class = alien_class
    def _create_alien(self, ...):
        alien = self.alien_class(self.screen, self.settings)  # flexível
```

### 3. `alien_invasion_refactored.py` — Switch de comportamento

Para usar alienígenas rápidos, basta passar `FastAlien` na inicialização:

```python
# Alien normal
self.fleet_manager = FleetManager(self.screen, self.settings, self.ship, Alien)

# Alien rápido — sem modificar FleetManager
self.fleet_manager = FleetManager(self.screen, self.settings, self.ship, FastAlien)
```

## Por que isso importa

Nenhum arquivo existente precisou ser reescrito para adicionar o novo comportamento. Para criar um `ShieldAlien`, `ZigZagAlien` ou qualquer outro tipo, basta:

1. Criar um novo arquivo que herda de `Alien`
2. Sobrescrever apenas o método que muda
3. Passar a nova classe para o `FleetManager`

Isso é OCP na prática: **extensão sem modificação**.
