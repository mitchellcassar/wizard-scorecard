import unittest
from unittest.mock import patch

from scorecard.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def test_player_initially_has_no_bid_total_or_name(self):

        self.assertEqual(self.player.name, '')
        self.assertEqual(self.player.bid, 0)
        self.assertEqual(self.player.total, 0)
    
    @patch ('builtins.input', return_value = 'mitchell')
    def test_player_can_receive_dynamic_name(self, mock_input):
        self.player.get_name()
        self.assertEqual(self.player.name, 'mitchell')
    
    def test_determines_one_player_greater_than_another(self):
        player2 = Player()

        self.player.total = 100
        player2.total = 150

        self.assertEqual(player2 > self.player, True)

    def test_sorts_players_by_total_properly(self):
        player2 = Player()
        player3 = Player()
        self.player.total = 200
        player2.total = 250
        player3.total = 100

        list_of_players = [
            self.player, player2, player3
        ]

        self.assertEqual(sorted(list_of_players), [
            player3, self.player, player2
        ])


        

