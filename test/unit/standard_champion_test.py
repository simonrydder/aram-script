import unittest
from datetime import date
from multiprocessing import Value

from src.enums import damage_type
from src.enums.damage_type import DamageType
from src.enums.range_type import RangeType
from src.enums.rating_scale import RatingScale
from src.enums.resource_type import ResourceType
from src.interfaces.champion import Champion
from src.standards.standard_rating import StandardRating
from src.standards.starndard_champion import StandardChampion


class TestStandardChampion(unittest.TestCase):
    def setUp(self) -> None:
        self.A = StandardChampion(
            name="Aatrox",
            release_date=date(2023, 6, 13),
            range_type=RangeType.MEELE,
            damage_type=DamageType.PHYSICAL,
            resource=ResourceType.MANALESS,
        )
        self.B = StandardChampion(
            name="Ahri",
            release_date=date(2020, 5, 19),
            range_type=RangeType.RANGED,
            damage_type=DamageType.MAGIC,
            resource=ResourceType.MANA,
        )
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

        with self.assertRaises(ValueError):
            self.A.release_date = new_date

        self.assertNotEqual(self.A.release_date, new_date)

    def test_that_range_type_is_Melee(self):
        self.assertEqual(self.A.range_type, RangeType.MEELE)

    def test_that_B_has_range_type_ranged(self):
        self.assertEqual(self.B.range_type, RangeType.RANGED)

    def test_that_range_type_cannot_be_changed(self):
        new_range_type = RangeType.RANGED
        with self.assertRaises(ValueError):
            self.A.range_type = new_range_type

        self.assertNotEqual(self.A.range_type, new_range_type)

    def test_that_damage_type_is_physical(self):
        self.assertEqual(self.A.damage_type, DamageType.PHYSICAL)

    def test_that_B_has_damage_type_magic(self):
        self.assertEqual(self.B.damage_type, DamageType.MAGIC)

    def test_that_damage_type_cannot_be_changed(self):
        new_dmg_type = DamageType.MAGIC
        with self.assertRaises(ValueError):
            self.A.damage_type = new_dmg_type

        self.assertNotEqual(self.A.damage_type, new_dmg_type)

    def test_that_resource_is_manaless(self):
        self.assertEqual(self.A.resource, ResourceType.MANALESS)

    def test_that_B_has_resource_mana(self):
        self.assertEqual(self.B.resource, ResourceType.MANA)

    def test_that_resource_cannot_be_changed(self):
        new_resource = ResourceType.ENERGY
        with self.assertRaises(ValueError):
            self.A.resource = new_resource

        self.assertNotEqual(self.A.resource, new_resource)

    # def test_that_ratings_is_3_3_2_2_2(self):
    #     rating = StandardRating(3, 3, 2, 2, 2)
