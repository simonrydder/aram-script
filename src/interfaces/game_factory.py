
from abc import ABC


class GameFactory(ABC):
    def __init__(self) -> None:
        pass

    def get_number_of_players(self) -> int:
        pass