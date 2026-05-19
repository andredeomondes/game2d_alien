import pygame

from settings import Settings
from ship import Ship
from bullet_manager import BulletManager
from fleet_manager import FleetManager
from game_events import GameEventHandler
from game_renderer import GameRenderer


class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""

    def __init__(self) -> None:
        """Construtor da classe que inicializa o jogo e cria os recursos básicos."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self.screen, self.settings)
        self.bg_color = self.settings.bg_color

        self.bullet_manager = BulletManager(self.screen, self.settings, self.ship)
        self.fleet_manager = FleetManager(self.screen, self.settings, self.ship)
        self.event_handler = GameEventHandler(self.ship, self.bullet_manager)

        self.renderer = GameRenderer(
            self.screen,
            self.bg_color,
            self.ship,
            self.bullet_manager.bullets,
            self.fleet_manager.aliens,
        )

    def run_game(self) -> None:
        """Inicia o laço principal do jogo."""
        self.fleet_manager.create_fleet()

        while True:
            self.event_handler._check_events()
            self._update_game_state()
            self.renderer._render_screen()

    def _update_game_state(self) -> None:
        """Atualiza as posições de todos os elementos."""
        self.ship.update()
        self.bullet_manager._update_bullets(self.fleet_manager.aliens)
        self.fleet_manager._update_aliens()


if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
