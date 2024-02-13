import unittest
from test.fixed_folder_strategy import fixed_folder_strategy

from src.enums.data_columns import DataColumn
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

    def test_that_basic_info_has_specific_columns(self):
        df = self.loader.basic_info()

        self.assertIn(DataColumn.NAME, df.columns)
        self.assertIn(DataColumn.RELEASE_DATE, df.columns)
        self.assertIn(DataColumn.IMG_FULL_SRC, df.columns)

    def test_that_ratings_has_10_rows(self):
        df = self.loader.ratings()

        self.assertEqual(len(df), 10)

    def test_that_ratings_has_6_columns(self):
        df = self.loader.ratings()

        self.assertEqual(len(df.columns), 6)

    def test_that_ratings_has_specific_columns(self):
        df = self.loader.ratings()

        self.assertIn(DataColumn.NAME, df.columns)
        self.assertIn(DataColumn.DMG, df.columns)
        self.assertIn(DataColumn.TOUGHNESS, df.columns)
        self.assertIn(DataColumn.CONTROL, df.columns)
        self.assertIn(DataColumn.MOBILITY, df.columns)
        self.assertIn(DataColumn.UTILITY, df.columns)
