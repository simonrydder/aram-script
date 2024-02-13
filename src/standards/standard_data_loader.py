import os
from typing import Literal

from pandas import DataFrame, read_csv  # type: ignore

from src.interfaces.data_loader import DataLoader  # type: ignore
from src.interfaces.folder_strategy import FolderStrategy


class StandardDataLoader(DataLoader):
    def __init__(self, folder_strategy: FolderStrategy) -> None:
        super().__init__(folder_strategy)

    def load_file(self, file: Literal["icons", "ratings", "stats"]) -> DataFrame:
        filename = f"lol-champ-{file}.csv"
        filepath = os.path.join(self.folder_strategy(), filename)
        return read_csv(filepath)

    def basic_info(self) -> DataFrame:
        raw = self.load_file("stats")
        result = raw.loc[:, ["name", "release-date", "image-full-src"]]
        return result


if __name__ == "__main__":
    from test.fixed_folder_strategy import fixed_folder_strategy

    StandardDataLoader(fixed_folder_strategy).basic_info()
