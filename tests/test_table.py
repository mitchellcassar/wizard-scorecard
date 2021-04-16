import unittest
from unittest.mock import patch
from scorecard.table import Table
from scorecard.player import Player

class TestTable(unittest.TestCase):

    def setUp(self):
        self.table = Table()
    
    @patch ('builtins.input', return_value = 3)
    def test_accepts_number_of_players(self, mock_input):
        self.table.accept_number_of_players()

        self.assertEqual(self.table.number_of_players, 3)

    @patch ('builtins.input', return_value = 2)
    def test_throws_error_if_number_of_players_outside_range(self,mock_input):
        with self.assertRaises(ValueError):
            self.table.accept_number_of_players()
    
    def test_calculates_number_of_hands_to_be_played(self):
        self.table.number_of_players = 5
        self.table.calculate_number_of_hands()

        self.assertEqual(self.table.number_of_hands, 12)

    def test_list_of_players_is_initially_empty(self):
        self.assertEqual(self.table.list_of_players, [])
    
    def test_can_append_player_objects_to_list_of_players(self):
        player = Player()
        self.table.list_of_players.append(player)

        self.assertEqual(self.table.list_of_players, [player])
    
    def test_instantiates_a_player_obj_for_every_player_in_list_of_players(self):
        self.table.number_of_players = 2
        self.table.create_player_objs()
        self.assertEqual(len(self.table.list_of_players), 2)
