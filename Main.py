from AlphaBetaPruning import AlphaBetaPruning

print('Choose your color')
print('1. White')
print('2. Black')

player_color = int(input()) == 1

alpha_beta = AlphaBetaPruning(player_color)

alpha_beta.start()