# Commit 1 — Criação do arquivo alien_invasion.py

**Branch:** `main`  
**Mensagem:** `feat: Criacao do arquivo alien_invasion.py`

## O que foi feito

Criação do arquivo principal do jogo com uma única classe `AlienInvasion`.

## Estrutura

```
src/
└── alien_invasion.py
```

## Código

```python
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
```

## Por que isso importa

Ponto de partida do projeto. A classe `AlienInvasion` inicializa o pygame, cria a janela e mantém o laço principal rodando até o usuário fechar o jogo.

O método `run_game` contém o **game loop**: o coração de qualquer jogo — ele roda infinitamente, lê eventos e atualiza a tela.
