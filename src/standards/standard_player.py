from src.interfaces.player import Player


class StandardPlayer(Player):
    def __init__(self, name: str) -> None:
        super().__init__(name)
