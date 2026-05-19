class GameStats:
    """Rastreia estatísticas do jogo Alien Invasion."""

    def __init__(self, settings) -> None:
        """Inicializa estatísticas."""
        self.settings = settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self) -> None:
        """Inicializa estatísticas que podem mudar durante o jogo."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
