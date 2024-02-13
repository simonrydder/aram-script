import unittest
from test.fixed_folder_strategy import fixed_folder_strategy

from src.standards.standard_data_loader import StandardDataLoader


class TestStandardDataLoaderStrategy(unittest.TestCase):
    def setUp(self) -> None:
        self.loader = StandardDataLoader(fixed_folder_strategy)
        return super().setUp()

    def test_that_loading_of_champion_ratings_has_10_rows(self):
        df = self.loader.load_file("ratings")

        self.assertEqual(len(df), 10)

    def test_that_loading_of_champion_ratings_has_9_columns(self):
        df = self.loader.load_file("ratings")

        self.assertEqual(len(df.columns), 9)

    def test_that_loading_of_champion_ratings_has_Aatrox_row_1_col_3(self):
        df = self.loader.load_file("ratings")
        name = df.iloc[0, 2]

        self.assertEqual(name, "Aatrox")

    def test_that_loading_of_champion_stats_has_10_rows(self):
        df = self.loader.load_file("stats")

        self.assertEqual(len(df), 10)

    def test_that_loading_of_champion_icons_has_ashe_last(self):
        df = self.loader.load_file("icons")
        name = df.iloc[9, 2]

        self.assertEqual(name, "Ashe")

    def test_that_basic_info_has_10_rows(self):
        df = self.loader.basic_info()

        self.assertEqual(len(df), 10)

    def test_that_basic_info_has_3_columns(self):
        df = self.loader.basic_info()

        self.assertEqual(len(df.columns), 3)

    def test_that_basic_info_has_column_name(self):
        df = self.loader.basic_info()

        self.assertIn("name", df.columns)

    def test_that_basic_info_has_column_release_date(self):
        df = self.loader.basic_info()

        self.assertIn("release-date", df.columns)
