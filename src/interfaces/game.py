from abc import ABC, abstractmethod

from src.interfaces.player import Player


class Game(ABC):

    def __init__(self) -> None:
        self.players: list[Player] = []
        pass

    @abstractmethod
    def add_player(self, name: str) -> None:
        pass

    @abstractmethod
    def remove_player(self, name: str) -> None:
        pass
