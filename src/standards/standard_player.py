from src.interfaces.player import Player


class StandardPlayer(Player):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def update_score(self, new_score: int) -> None:
        if new_score < 0:
            raise ValueError("Score cannot be negative")

        self.score = new_score
