from db import Database
from gameview import GameView
from player import Player


class Game:
    """
    Main game controller class.

    Methods:
        game_loop: Run the game loop asynchronously
    """

    def __init__(self, player1: Player, player2: Player) -> None:
        """
        Initialize the game with players, a database wrapper object,
        and a game view object.

        Args:
            player1:

        """
        self.db: Database = Database()
        self.view: GameView = GameView()
        self.player1 = player1
        self.player2 = player2
        self._state = [None for _ in range(9)]

    async def game_loop(self) -> None: ...
