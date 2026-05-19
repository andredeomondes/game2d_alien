# Commits 3 e 4 — Refatoração aplicando SRP

**Branch:** `feature/applying-solid`  
**Mensagens:**
- `refatoração do código: aplicando SRP`
- `refactor: adiciona type hints e extrai _create_alien`

## O que é SRP (Single Responsibility Principle)

> "Uma classe deve ter apenas uma razão para mudar."

É o **S** do SOLID. Cada classe ou módulo deve ter **uma única responsabilidade**.

## Problema antes

A classe `AlienInvasion` fazia tudo:
- Lia eventos do teclado
- Atualizava a nave
- Atualizava os projéteis
- Atualizava os alienígenas
- Verificava colisões
- Desenhava a tela

Se qualquer dessas áreas precisasse mudar, você mexia na mesma classe — aumentando risco de quebrar outra coisa.

## O que foi feito

A lógica foi dividida em **métodos privados** com responsabilidades claras:

```python
def run_game(self) -> None:
    self.create_fleet()
    while True:
        self._check_events()       # só lida com eventos
        self._update_game_state()  # só atualiza estado
        self._render_screen()      # só desenha
```

### Métodos extraídos

| Método | Responsabilidade |
|---|---|
| `_check_events` | Lê eventos do pygame |
| `_handle_keydown` | Trata tecla pressionada |
| `_handle_keyup` | Trata tecla solta |
| `_fire_bullet` | Cria projétil |
| `_update_game_state` | Orquestra updates |
| `_update_bullets` | Atualiza projéteis |
| `_remove_offscreen_bullets` | Remove projéteis fora da tela |
| `_check_bullet_alien_collisions` | Colisão projétil/alien |
| `_update_aliens` | Atualiza frota |
| `_check_fleet_edges` | Detecta borda |
| `_change_fleet_direction` | Muda direção da frota |
| `_check_ship_collision` | Colisão nave/alien |
| `create_fleet` | Cria a frota completa |
| `_create_alien` | Cria e posiciona um alien |
| `_render_screen` | Desenha tudo |
| `_draw_bullets` | Desenha projéteis |

## Por que isso importa

Cada método faz **uma coisa só**. Isso facilita:
- Encontrar bugs (você sabe onde olhar)
- Testar partes isoladas
- Modificar sem quebrar o resto
