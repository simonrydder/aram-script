import os

from pandas import DataFrame, read_csv  # type: ignore

from src.interfaces.folder_strategy import FolderStrategy


def standard_data_loader(file: str, data_folder: FolderStrategy) -> DataFrame:
    return read_csv(os.path.join(data_folder(), file))
