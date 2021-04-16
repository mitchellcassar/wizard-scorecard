from scorecard.player import Player

class Table():
    def __init__(self):
        self.number_of_players = 0
        self.number_of_hands = 0
        self.list_of_players = []

    def accept_number_of_players(self):
        self.number_of_players = int(input('how many players? '))
        if self.number_of_players not in range(3,7):
            raise ValueError('please enter a number of players between 3 and 6')


    def calculate_number_of_hands(self):
        self.number_of_hands = 60 / self.number_of_players

    def create_player_objs(self):
        self.list_of_players = [Player() for num in range(0, self.number_of_players)]


