from abc import ABC, abstractmethod
from typing import Literal

from pandas import DataFrame

from src.interfaces.folder_strategy import FolderStrategy


class DataLoader(ABC):
    def __init__(self, folder_strategy: FolderStrategy) -> None:
        super().__init__()
        self.folder_strategy = folder_strategy

    @abstractmethod
    def load_file(self, file: Literal["icons", "ratings", "stats"]) -> DataFrame:
        pass

    @abstractmethod
    def basic_info(self) -> DataFrame:
        pass

    @abstractmethod
    def ratings(self) -> DataFrame:
        pass
