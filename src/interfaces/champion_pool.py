from abc import ABC, abstractmethod
from typing import Self

from pandas import DataFrame

from src.interfaces.champion import Champion
from src.interfaces.folder_strategy import FolderStrategy


class ChampionPool(ABC):
    def __init__(self, folder_strategy: FolderStrategy) -> None:
        super().__init__()
        self._champs = None
        self._folder_strategy = folder_strategy

    @property
    @abstractmethod
    def champs(self) -> list[Champion]:
        pass

    @champs.setter
    @abstractmethod
    def champs(self, new_pool: list[Champion]) -> None:
        pass

    @abstractmethod
    def generate_champion_pool(self) -> Self:
        pass

    @abstractmethod
    def load_champion_data(self) -> DataFrame:
        pass
