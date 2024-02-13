import unittest
from test.factories.champion.a_champion_factory import TestAChampionFactory
from test.factories.champion.b_champion_factory import TestBChampionFactory
from test.fixed_folder_strategy import fixed_folder_strategy

from src.standards.standard_champion import StandardChampion
from src.standards.standard_champion_pool import StandardChampionPool


class TestStandardChampionPool(unittest.TestCase):
    def setUp(self) -> None:
        self.cp = StandardChampionPool(fixed_folder_strategy)
        return super().setUp()

    def test_that_champion_pool_has_test_champ_a(self):
        champ1 = StandardChampion(TestAChampionFactory())
        self.cp.champs = [champ1]
        champs = self.cp.champs
        self.assertEqual(champs[0], champ1)

    def test_that_champion_pool_has_one_champ(self):
        champ1 = StandardChampion(TestAChampionFactory())
        self.cp.champs = [champ1]

        self.assertEqual(len(self.cp.champs), 1)

    def test_that_champion_pool_has_two_champs(self):
        c1 = StandardChampion(TestAChampionFactory())
        c2 = StandardChampion(TestBChampionFactory())
        self.cp.champs = [c1, c2]

        self.assertEqual(len(self.cp.champs), 2)

    @unittest.skip  # type: ignore
    def test_that_load_champion_data_has_10_rows(self):
        df = self.cp.load_champion_data()

        self.assertEqual(len(df), 10)
