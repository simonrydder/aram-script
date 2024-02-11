from src.interfaces.game_factory import GameFactory


class AlphaAramFactory(GameFactory):
    def __init__(self) -> None:
        pass

    def get_number_of_players(self) -> int:
        return 6
