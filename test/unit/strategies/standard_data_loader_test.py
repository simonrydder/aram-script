import unittest
from test.fixed_folder_strategy import fixed_folder_strategy

from src.standards.standard_data_loader import standard_data_loader


class TestStandardDataLoaderStrategy(unittest.TestCase):
    def setUp(self) -> None:
        self.folder_strategy = fixed_folder_strategy
        self.func = standard_data_loader
        return super().setUp()

    def test_that_loading_of_champion_ratings_has_10_rows(self):
        df = self.func("lol-champ-ratings.csv", self.folder_strategy)

        self.assertEqual(len(df), 10)

    def test_that_loading_of_champion_ratings_has_9_columns(self):
        df = self.func("lol-champ-ratings.csv", self.folder_strategy)

        self.assertEqual(len(df.columns), 9)

    def test_that_loading_of_champion_ratings_has_Aatrox_row_1_col_3(self):
        df = self.func("lol-champ-ratings.csv", self.folder_strategy)
        name = df.iloc[0, 2]

        self.assertEqual(name, "Aatrox")

    def test_that_loading_of_champion_stats_has_10_rows(self):
        df = self.func("lol-champ-stats.csv", self.folder_strategy)

        self.assertEqual(len(df), 10)

    def test_that_loading_of_champion_icons_has_ashe_last(self):
        df = self.func("lol-champ-icons.csv", self.folder_strategy)
        name = df.iloc[9, 2]

        self.assertEqual(name, "Ashe")
