from ChessEngine import ChessEngine
import random


class RandomEngine(ChessEngine):
    def __init__(self, player_color):
        super().__init__(player_color)
    
    def _computer_move(self):
        choice = random.choice(list(self._board.legal_moves))

        return choice