import asyncio
from unittest.mock import MagicMock

from player import Move, Player


def test_should_make_move_valid(monkeypatch):
    responses = iter(["1", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    p = Player("test")
    m = asyncio.run(p.make_move())

    assert m == Move(1, 3)


def test_should_retry_until_valid(monkeypatch):

    fake_move = MagicMock(side_effect=["lalal", "9", "1", "3"])
    monkeypatch.setattr("builtins.input", fake_move)

    p = Player("test")
    m = asyncio.run(p.make_move())

    assert m == Move(1, 3)
    assert fake_move.call_count == 4
