import os
from typing import Literal

from pandas import DataFrame, read_csv  # type: ignore

from src.enums.data_columns import DataColumn
from src.interfaces.data_loader import DataLoader
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
        result = raw.loc[
            :, [DataColumn.NAME, DataColumn.RELEASE_DATE, DataColumn.IMG_FULL_SRC]
        ]
        return result

    def ratings(self) -> DataFrame:
        return self.load_file("ratings").loc[
            :,
            [
                DataColumn.NAME,
                DataColumn.DMG,
                DataColumn.TOUGHNESS,
                DataColumn.CONTROL,
                DataColumn.MOBILITY,
                DataColumn.UTILITY,
            ],
        ]


if __name__ == "__main__":
    from test.fixed_folder_strategy import fixed_folder_strategy

    data = StandardDataLoader(fixed_folder_strategy).ratings()
    pass
