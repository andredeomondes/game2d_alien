import pygame


class GameRenderer:
    """Responsável por desenhar os elementos do jogo na tela."""

    def __init__(self, screen, bg_color, ship, bullets, aliens, scoreboard) -> None:
        self.screen = screen
        self.bg_color = bg_color
        self.ship = ship
        self.bullets = bullets
        self.aliens = aliens
        self.scoreboard = scoreboard

    def _render_screen(self) -> None:
        """Redesenha a tela a cada passagem pelo laço."""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.scoreboard.show_score()
        pygame.display.flip()
