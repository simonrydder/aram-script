from abc import ABC


class Player(ABC):
    def __init__(
        self,
        name: str,
    ) -> None:
        self.name = name
