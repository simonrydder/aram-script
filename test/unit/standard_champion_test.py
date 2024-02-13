import unittest
from datetime import date
from test.factories.champion.a_champion_factory import TestAChampionFactory
from test.factories.champion.b_champion_factory import TestBChampionFactory

from src.enums.damage_type import DamageType
from src.enums.range_type import RangeType
from src.enums.resource_type import ResourceType
from src.standards.standard_champion import StandardChampion
from src.standards.standard_rating import StandardRating


class TestStandardChampion(unittest.TestCase):
    def setUp(self) -> None:
        self.A = StandardChampion(TestAChampionFactory())
        self.B = StandardChampion(TestBChampionFactory())
        return super().setUp()

    def test_that_name_is_Aatrox(self):
        self.assertEqual(self.A.name, "Aatrox")

    def test_that_B_has_name_Ahri(self):
        self.assertEqual(self.B.name, "Ahri")

    def test_that_name_cannot_be_changed(self):
        with self.assertRaises(ValueError):
            self.A.name = "Ahri"

        self.assertEqual(self.A.name, "Aatrox")

    def test_that_release_date_is_2023_06_13(self):
        self.assertEqual(self.A.release_date, date(2023, 6, 13))

    def test_that_B_has_release_date_2020_05_19(self):
        self.assertEqual(self.B.release_date, date(2020, 5, 19))

    def test_that_release_date_cannot_be_changed(self):
        new_date = date(1, 1, 1)
        old_date = self.A.release_date

        with self.assertRaises(ValueError):
            self.A.release_date = new_date

        self.assertEqual(self.A.release_date, old_date)

    def test_that_range_type_is_Melee(self):
        self.assertEqual(self.A.range_type, RangeType.MEELE)

    def test_that_B_has_range_type_ranged(self):
        self.assertEqual(self.B.range_type, RangeType.RANGED)

    def test_that_range_type_cannot_be_changed(self):
        new_range_type = RangeType.RANGED
        old_range_type = self.A.range_type

        with self.assertRaises(ValueError):
            self.A.range_type = new_range_type

        self.assertEqual(self.A.range_type, old_range_type)

    def test_that_damage_type_is_physical(self):
        self.assertEqual(self.A.damage_type, DamageType.PHYSICAL)

    def test_that_B_has_damage_type_magic(self):
        self.assertEqual(self.B.damage_type, DamageType.MAGIC)

    def test_that_damage_type_cannot_be_changed(self):
        new_dmg_type = DamageType.MAGIC
        old_dmg_type = self.A.damage_type
        with self.assertRaises(ValueError):
            self.A.damage_type = new_dmg_type

        self.assertEqual(self.A.damage_type, old_dmg_type)

    def test_that_resource_is_manaless(self):
        self.assertEqual(self.A.resource, ResourceType.MANALESS)

    def test_that_B_has_resource_mana(self):
        self.assertEqual(self.B.resource, ResourceType.MANA)

    def test_that_resource_cannot_be_changed(self):
        new_resource = ResourceType.ENERGY
        old_resource = self.A.resource
        with self.assertRaises(ValueError):
            self.A.resource = new_resource

        self.assertEqual(self.A.resource, old_resource)

    def test_that_A_has_rating_1_2_3_3_3(self):
        self.assertEqual(self.A.rating, StandardRating(1, 2, 3, 3, 3))

    def test_that_B_has_rating_2_1_2_1_1(self):
        self.assertEqual(self.B.rating, StandardRating(2, 1, 2, 1, 1))

    def test_that_ratings_cannot_be_changed(self):
        new_rating = StandardRating(1, 1, 1, 1, 1)
        old_rating = self.A.rating
        with self.assertRaises(ValueError):
            self.A.rating = new_rating

        self.assertEqual(self.A.rating, old_rating)
