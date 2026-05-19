# Commit 7 — Pontuação, Vidas e Controle de FPS

**Branch:** `feature/applying-solid`  
**Mensagem:** `refactor: aplicando princípio SOLID`

## O que foi feito

Adicionados `GameStats`, `Scoreboard`, controle de FPS com `Clock`, e atualização do `GameRenderer`.

## Novos arquivos

### `game_stats.py` — GameStats

Centraliza o **estado do jogo** em um único lugar:

```python
class GameStats:
    def __init__(self, settings) -> None:
        self.reset_stats()
        self.game_active = True   # controla se o jogo está rodando

    def reset_stats(self) -> None:
        self.ships_left = self.settings.ship_limit
        self.score = 0
```

**Por que importa:** antes, variáveis como `score` e `ships_left` estariam espalhadas. Com `GameStats`, qualquer parte do jogo acessa ou modifica o estado passando por um único objeto.

### `scoreboard.py` — Scoreboard

Transforma o número da pontuação em uma **imagem renderizada** pelo pygame:

```python
def prep_score(self) -> None:
    score_str = str(self.stats.score)
    self.score_image = self.font.render(score_str, True, self.text_color, bg_color)
    self.score_rect.right = self.screen_rect.right - 20
    self.score_rect.top = 20
```

O método `prep_score` é chamado sempre que a pontuação muda — ele regera a imagem. `show_score` apenas desenha a imagem já preparada.

## Arquivos atualizados

### `game_renderer.py`

Recebe `scoreboard` como dependência e chama `show_score()` antes do `flip()`:

```python
def _render_screen(self) -> None:
    self.screen.fill(self.bg_color)
    self.ship.blitme()
    self.aliens.draw(self.screen)
    for bullet in self.bullets.sprites():
        bullet.draw_bullet()
    self.scoreboard.show_score()   # novo
    pygame.display.flip()
```

### `bullet_manager.py`

`_check_bullet_alien_collisions` agora **retorna** o dict de colisões, separado de `_update_bullets`:

```python
def _check_bullet_alien_collisions(self, aliens) -> dict:
    return pygame.sprite.groupcollide(self.bullets, aliens, True, True)
```

Isso permite que `AlienInvasion` use as colisões para incrementar a pontuação.

### `alien_invasion_refactored.py`

Três mudanças principais:

**1. Clock para controle de FPS:**
```python
self.clock = pygame.time.Clock()
# ...
self.clock.tick(60)  # no final do loop
```
Garante que o jogo rode a no máximo 60 frames por segundo em qualquer máquina.

**2. Verificação de `game_active`:**
```python
if self.stats.game_active:
    self.ship.update()
    self._update_game_state()
```
Quando `game_active = False`, o jogo para de atualizar mas continua renderizando (útil para tela de game over).

**3. Pontuação por colisão:**
```python
collisions = self.bullet_manager._check_bullet_alien_collisions(self.fleet_manager.aliens)
if collisions:
    self.stats.score += self.settings.alien_points * len(collisions)
    self.sb.prep_score()
```
Cada alien abatido soma `alien_points` à pontuação e atualiza a imagem do placar.
