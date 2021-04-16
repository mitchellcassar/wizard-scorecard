from scorecard.table import Table
from scorecard.player import Player
from scorecard.functions import Functions

table = Table()
table.accept_number_of_players()
table.calculate_number_of_hands()
print(f'\n There will be {table.number_of_hands} rounds played.')
table.create_player_objs()

for player in table.list_of_players:
    player.get_name()

functions = Functions()


round = 1
cards = 1

while round <= table.number_of_hands:

    print(f'\n this is round {round}.')
    print(f'\n each player will get {cards} cards.')

    functions.bidding_round(table.list_of_players)
    functions.input_tricks_taken(table.list_of_players)
    functions.calculate_round_results(table.list_of_players)
    for player in table.list_of_players:
        print(f"\n {player.name}'s total after round {round} is {player.total}")


    round += 1
    cards += 1

sorted_by_final_score = sorted(table.list_of_players, reverse = True)

print(f"\n today's winner is {sorted_by_final_score[0].name}")

for player in sorted_by_final_score:
    print(f"\n {player.name}'s final score: {player.total}")


print('Thanks for Playing!')


