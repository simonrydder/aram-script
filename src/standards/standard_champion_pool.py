from typing import Self

from pandas import DataFrame

from src.interfaces.champion import Champion
from src.interfaces.champion_pool import ChampionPool
from src.interfaces.folder_strategy import FolderStrategy


class StandardChampionPool(ChampionPool):
    def __init__(self, folder_strategy: FolderStrategy) -> None:
        super().__init__(folder_strategy)

    @property
    def champs(self) -> list[Champion]:
        return self._champs

    @champs.setter
    def champs(self, new_pool: list[Champion]) -> None:
        self._champs = new_pool

    def generate_champion_pool(self) -> Self:
        return super().generate_champion_pool()

    def load_champion_data(self) -> DataFrame:
        return super().load_champion_data()
