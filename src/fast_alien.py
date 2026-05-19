from alien import Alien


class FastAlien(Alien):
    """Alienígena mais rápido que herda da classe Alien."""

    def update(self) -> None:
        """Move o alienígena mais rápido para a direita ou esquerda."""
        self.x += (self.settings.alien_speed * 2) * self.settings.fleet_direction
        self.rect.x = self.x
