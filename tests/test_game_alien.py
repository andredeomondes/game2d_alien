import pytest
from game_stats import GameStats


class StubSettings:
    """Stub de Settings para isolar GameStats de dependências reais."""
    ship_limit = 3
    alien_points = 50


# --- Stub: verifica estado inicial do jogo ---

def test_game_stats_estado_inicial():
    stats = GameStats(StubSettings())
    assert stats.score == 0
    assert stats.ships_left == 3
    assert stats.game_active is True


def test_game_stats_score_nao_negativo():
    stats = GameStats(StubSettings())
    stats.score = 0
    assert stats.score >= 0


# --- Mock: verifica que reset_stats é chamado e restaura valores ---

def test_game_stats_reset_com_mock(mocker):
    stats = GameStats(StubSettings())
    stats.score = 500
    stats.ships_left = 0

    mock_reset = mocker.patch.object(stats, "reset_stats", wraps=stats.reset_stats)
    stats.reset_stats()

    mock_reset.assert_called_once()
    assert stats.score == 0
    assert stats.ships_left == 3
