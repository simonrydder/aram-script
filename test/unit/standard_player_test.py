import unittest

from src.standards.standard_player import StandardPlayer


class TestStandardPlayer(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_player_has_name_p1(self):
        player = StandardPlayer("p1")
        self.assertEqual(player.name, "p1")

    def test_player_has_name_p2(self):
        player = StandardPlayer("p2")
        self.assertEqual(player.name, "p2")
