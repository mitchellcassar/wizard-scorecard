class Functions():
    def __init__(self):
        pass

    def bidding_round(self, list_of_players):
        for player in list_of_players:
            player.bid = int(input(f'how many tricks is {player.name} going to take? '))

    def input_tricks_taken(self, list_of_players):
        for player in list_of_players:
            player.tricks_taken = int(input(f'how many tricks did {player.name} take? '))


    def calculate_round_results(self, list_of_players):
        for player in list_of_players:
            if player.bid == player.tricks_taken:
                player.total += 20 + (player.bid * 10)
            if player.bid != player.tricks_taken:
                player.total -= abs(player.bid - player.tricks_taken) * 10
