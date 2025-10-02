import asyncio
from dataclasses import dataclass
from typing import NamedTuple


class Move(NamedTuple):
    """
    Move class for storing row and column of a move.

    Attributes:
        row: integer from 1-3
        col: integer from 1-3
    """

    row: int
    col: int


@dataclass
class Player:
    """
    Player class for handling player interactions.

    Attributes:
        name: player's name

    Methods:
        make_move: Get a move from the player
    """

    name: str

    async def make_move(self) -> Move:
        """
        Prompt the player for a move asynchronously.

        Iterate until valid inputs (ints from 1-3) are provided.

        Returns:
            Move: The player's move with row and column from 1-3.
        """
        while True:
            # Run input in a separate thread to avoid blocking.
            row = await asyncio.to_thread(input, f"{self.name}, Enter Row (1-3)")
            col = await asyncio.to_thread(input, f"{self.name}, Enter Col (1-3)")
            try:
                row = int(row)
                col = int(col)
                if 1 <= row <= 3 and 1 <= col <= 3:
                    return Move(row, col)
            except ValueError:
                print("Invalid inputs. Enter valid row and column from 1-3.")
