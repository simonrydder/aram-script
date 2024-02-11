from src.interfaces.game import Game
from src.interfaces.game_factory import GameFactory
from src.interfaces.player import Player
from src.standards.standard_player import StandardPlayer


class StandardGame(Game):
    def __init__(self, game_factory: GameFactory) -> None:
        super().__init__(game_factory)

    def add_player(self, name: str) -> None:
        player_with_name = self._find_player(name)
        if not player_with_name:
            new_player = StandardPlayer(name)
            self.players.append(new_player)

    def remove_player(self, name: str) -> None:
        player_to_remove = self._find_player(name)
        if player_to_remove:
            self.players.remove(player_to_remove)

    def _find_player(self, name: str) -> Player | None:
        for player in self.players:
            if player.name == name:
                return player

        return None
