import unittest

from src.standards.standard_player import StandardPlayer


class TestStandardPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.player = StandardPlayer("player")

    def test_player_has_name_p1(self):
        player = StandardPlayer("p1")

        self.assertEqual(player.name, "p1")

    def test_player_has_name_p2(self):
        player = StandardPlayer("p2")

        self.assertEqual(player.name, "p2")

    def test_player_has_score_0(self):
        score = self.player.score

        self.assertEqual(score, 0)

    def test_player_update_score_to_1(self):
        self.player.update_score(1)
        score = self.player.score

        self.assertEqual(score, 1)

    def test_player_update_score_to_2(self):
        self.player.update_score(2)
        score = self.player.score

        self.assertEqual(score, 2)

    def test_player_update_score_to_negative_1(self):
        # Checks that trying to update score to negative value raises ValueError
        with self.assertRaises(ValueError):
            self.player.update_score(-1)

        # Checks that score has not been updated.
        score = self.player.score

        self.assertEqual(score, 0)

    def test_player_update_score_to_negative_10(self):
        # Checks that trying to update score to negative value raises ValueError
        with self.assertRaises(ValueError):
            self.player.update_score(-10)

        # Checks that score has not been updated.
        score = self.player.score

        self.assertEqual(score, 0)
