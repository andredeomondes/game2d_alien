import pygame

from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from bullet_manager import BulletManager
from fleet_manager import FleetManager
from game_events import GameEventHandler
from game_renderer import GameRenderer
from fast_alien import FastAlien


class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""

    def __init__(self) -> None:
        """Construtor da classe que inicializa o jogo e cria os recursos básicos."""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self.settings)
        self.ship = Ship(self.screen, self.settings)
        self.bg_color = self.settings.bg_color
        self.sb = Scoreboard(self.screen, self.settings, self.stats)

        self.bullet_manager = BulletManager(self.screen, self.settings, self.ship)
        self.fleet_manager = FleetManager(
            self.screen, self.settings, self.ship, FastAlien
        )
        self.event_handler = GameEventHandler(self.ship, self.bullet_manager)
        self.renderer = GameRenderer(
            self.screen,
            self.bg_color,
            self.ship,
            self.bullet_manager.bullets,
            self.fleet_manager.aliens,
            self.sb,
        )

    def run_game(self) -> None:
        """Inicia o laço principal do jogo."""
        self.fleet_manager.create_fleet()

        while True:
            self.event_handler._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_game_state()

            self.renderer._render_screen()
            self.clock.tick(60)

    def _update_game_state(self) -> None:
        """Atualiza as posições de todos os elementos e verifica pontuação."""
        self.bullet_manager._update_bullets(self.fleet_manager.aliens)
        self.fleet_manager._update_aliens()

        collisions = self.bullet_manager._check_bullet_alien_collisions(
            self.fleet_manager.aliens
        )
        if collisions:
            self.stats.score += self.settings.alien_points * len(collisions)
            self.sb.prep_score()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
