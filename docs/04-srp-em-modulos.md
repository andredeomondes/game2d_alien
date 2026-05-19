# Commit 5 — SRP em módulos separados

**Branch:** `feature/applying-solid`  
**Mensagem:** `refactor: finalização da refatoração para o princípio SRP`

## O que foi feito

O SRP foi levado ao próximo nível: cada responsabilidade virou um **arquivo separado**.

## Estrutura antes

```
src/
└── alien_invasion.py   ← fazia tudo
```

## Estrutura depois

```
src/
├── alien_invasion_refactored.py  ← orquestrador
├── bullet_manager.py             ← responsável pelos projéteis
├── fleet_manager.py              ← responsável pela frota
├── game_events.py                ← responsável pelos eventos
└── game_renderer.py              ← responsável pelo desenho
```

## Cada módulo

### `bullet_manager.py` — BulletManager
Gerencia tudo relacionado a projéteis:
- Criar um projétil quando o jogador aperta espaço
- Mover os projéteis a cada frame
- Remover projéteis que saíram da tela
- Detectar colisão entre projéteis e alienígenas

### `fleet_manager.py` — FleetManager
Gerencia a frota de alienígenas:
- Criar a frota completa no início do jogo
- Mover todos os alienígenas
- Detectar quando a frota chega na borda e mudar de direção
- Detectar colisão entre alienígenas e a nave

### `game_events.py` — GameEventHandler
Lê e trata entradas do usuário:
- Fechar a janela
- Pressionar setas (mover nave)
- Pressionar espaço (atirar)

### `game_renderer.py` — GameRenderer
Desenha todos os elementos na tela:
- Fundo
- Nave
- Alienígenas
- Projéteis

### `alien_invasion_refactored.py` — AlienInvasion
Orquestra os managers — não faz nada diretamente, só coordena:

```python
def run_game(self) -> None:
    self.fleet_manager.create_fleet()
    while True:
        self.event_handler._check_events()
        self._update_game_state()
        self.renderer._render_screen()
```

## Por que isso importa

Agora cada arquivo tem **uma única razão para existir**. Para mudar como os projéteis funcionam, você abre só `bullet_manager.py`. Para mudar como a tela é desenhada, só `game_renderer.py`. Nenhuma mudança afeta os outros arquivos.
