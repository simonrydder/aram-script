import unittest

from src.enums.rating_scale import RatingScale
from src.standards.standard_rating import StandardRating


class TestStandardRating(unittest.TestCase):
    def setUp(self) -> None:
        self.rating_a = StandardRating(
            damage=RatingScale.ONE,
            toughness=RatingScale.TWO,
            control=RatingScale.TREE,
            mobility=RatingScale.ONE,
            utility=RatingScale.TREE,
        )

        self.rating_b = StandardRating(
            damage=RatingScale.TWO,
            toughness=RatingScale.TREE,
            control=RatingScale.TWO,
            mobility=RatingScale.TREE,
            utility=RatingScale.ONE,
        )
        return super().setUp()

    def test_that_damage_is_1(self):
        self.assertEqual(self.rating_a.damage, 1)

    def test_that_toughness_is_2(self):
        self.assertEqual(self.rating_a.toughness, 2)

    def test_that_control_is_3(self):
        self.assertEqual(self.rating_a.control, 3)

    def test_that_mobility_is_1(self):
        self.assertEqual(self.rating_a.mobility, 1)

    def test_that_utility_is_3(self):
        self.assertEqual(self.rating_a.utility, 3)

    def test_that_damage_is_2(self):
        self.assertEqual(self.rating_b.damage, 2)

    def test_that_toughness_is_3(self):
        self.assertEqual(self.rating_b.toughness, 3)

    def test_that_control_is_2(self):
        self.assertEqual(self.rating_b.control, 2)

    def test_that_mobility_is_3(self):
        self.assertEqual(self.rating_b.mobility, 3)

    def test_that_utility_is_1(self):
        self.assertEqual(self.rating_b.utility, 1)

    def test_that_rating_a_is_equal_rating_1_2_3_1_3(self):
        new_rating = StandardRating(
            RatingScale.ONE,
            RatingScale.TWO,
            RatingScale.TREE,
            RatingScale.ONE,
            RatingScale.TREE,
        )

        self.assertEqual(self.rating_a, new_rating)

    def test_that_rating_a_has_total_rating_10(self):
        total = self.rating_a.total
        self.assertEqual(total, 10)

    def test_that_rating_b_has_total_rating_11(self):
        self.assertEqual(self.rating_b.total, 11)

    def test_that_rating_b_is_greater_than_rating_a(self):
        is_rating_b_greater = self.rating_b > self.rating_a
        self.assertEqual(is_rating_b_greater, True)

    def test_that_rating_a_is_not_greater_thhan_rating_b(self):
        is_rating_a_greater = self.rating_a > self.rating_b
        self.assertEqual(is_rating_a_greater, False)
