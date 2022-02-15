from RandomEngine import RandomEngine

print('Choose your color')
print('1. White')
print('2. Black')

player_color = int(input()) == 1

random_game = RandomEngine(player_color)

random_game.start()