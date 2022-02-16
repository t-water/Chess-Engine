from BruteForce import BruteForce

print('Choose your color')
print('1. White')
print('2. Black')

player_color = int(input()) == 1

brute_force = BruteForce(player_color)

brute_force.start()