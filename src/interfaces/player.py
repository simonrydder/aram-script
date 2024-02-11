from abc import ABC


class Player(ABC):
    def __init__(
        self,
        name: str,
    ) -> None:
        self.name = name
        self.score = 0

    def update_score(self, new_score: int) -> None:
        pass
