from abc import ABC

from src.interfaces.game_factory import GameFactory
from src.interfaces.player import Player


class Game(ABC):

    def __init__(self, game_factory: GameFactory) -> None:
        self.players: list[Player] = []
        pass

    def add_player(self, name: str) -> None:
        pass

    def remove_player(self, name: str) -> None:
        pass
