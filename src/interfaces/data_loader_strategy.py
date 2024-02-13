from typing import Callable

from pandas import DataFrame

from src.interfaces.folder_strategy import FolderStrategy

DataLoaderStrategy = Callable[[str, FolderStrategy], DataFrame]
