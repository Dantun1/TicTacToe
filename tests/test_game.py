from game import Game
from unittest.mock import MagicMock

def test_initialize_game_with_players():
    p1 = object()
    p2 = object()
    g = Game(p1, p2)

    assert g.player1 is p1
    assert g.player2 is p2
