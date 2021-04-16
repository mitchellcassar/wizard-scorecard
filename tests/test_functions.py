import unittest
from unittest.mock import patch

from scorecard.player import Player
from scorecard.functions import Functions

class TestFunctions(unittest.TestCase):
    
    def setUp(self):
        self.player = Player()
        self.list_of_players = [self.player]
        self.function = Functions()
    
    @patch ('builtins.input', return_value = 2)
    def test_input_overwrites_bid_for_player(self, mock_input):
        self.function.bidding_round(self.list_of_players)
        
        self.assertEqual(self.player.bid, 2)
    
    
    @patch ('builtins.input', return_value = 3)
    def test_accepts_input_of_tricks_taken(self, mock_input):
        self.function.input_tricks_taken(self.list_of_players)
        
        self.assertEqual(self.player.tricks_taken, 3)

    def test_calculates_round_results_when_bid_equals_tricks_taken(self):
        self.player.bid = 2
        self.player.tricks_taken = 2
        self.function.calculate_round_results(self.list_of_players)

        self.assertEqual(self.player.total, 40)
    
    def test_calculates_round_results_when_bid_doesnt_equal_tricks_taken(self):
        self.player.bid = 0
        self.player.tricks_taken = 2

        self.function.calculate_round_results(self.list_of_players)

        self.assertEqual(self.player.total, -20)


