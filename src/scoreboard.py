import pygame.font


class Scoreboard:
    """Uma classe para reportar informações de pontuação."""

    def __init__(self, screen, settings, stats) -> None:
        """Inicializa os atributos de pontuação."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self) -> None:
        """Transforma a pontuação em uma imagem renderizada."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self) -> None:
        """Desenha a pontuação na tela."""
        self.screen.blit(self.score_image, self.score_rect)
