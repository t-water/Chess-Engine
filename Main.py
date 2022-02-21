from TrainedEngine import TrainedEngine

print('Choose your color')
print('1. White')
print('2. Black')

player_color = int(input()) == 1

trained_engine = TrainedEngine(player_color)

trained_engine.start()