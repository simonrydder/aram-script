import unittest

from src.exceptions.max_player_reached_error import MaxPlayerReachedError
from src.standards.factories.alpha_aram_factory import AlphaAramFactory
from src.standards.standard_game import StandardGame


class TestStandardGame(unittest.TestCase):
    def setUp(self) -> None:
        self.game = StandardGame(AlphaAramFactory())

    def test_that_player_list_is_empty_at_initialization(self):
        players = self.game.players

        self.assertIsInstance(players, list)
        self.assertEqual(len(players), 0)

    def test_that_adding_one_player_append_list(self):
        self.game.add_player("p1")
        players = self.game.players

        self.assertEqual(len(players), 1)

    def test_that_adding_two_players_append_list(self):
        self.game.add_player("p1")
        self.game.add_player("p2")
        players = self.game.players

        self.assertEqual(len(players), 2)

    def test_that_adding_players_with_same_name_don_not_append_list(self):
        self.game.add_player("p1")
        self.game.add_player("p1")

        players = self.game.players

        self.assertEqual(len(players), 1)

    def test_that_p1_can_be_removed_from_players_with_p1(self):
        self.game.add_player("p1")
        self.game.remove_player("p1")
        players = self.game.players

        self.assertEqual(len(players), 0)

    def test_that_p2_cannot_be_removed_from_player_with_p1(self):
        self.game.add_player("p1")
        self.game.remove_player("p2")
        players = self.game.players

        self.assertEqual(len(players), 1)

    def test_that_max_4_players_are_allowed(self):
        # Add 4 players to the game
        for i in range(4):
            self.game.add_player(f"player_{i}")

        with self.assertRaises(MaxPlayerReachedError):
            self.game.add_player("5th_player")

        players = self.game.players
        self.assertEqual(len(players), 4)
