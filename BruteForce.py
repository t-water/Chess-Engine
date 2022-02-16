from ChessEngine import ChessEngine
import random


class BruteForce(ChessEngine):
    def __init__(self, player_color):
        super().__init__(player_color)

        self.__position_evaluations = {}
    
    def _computer_move(self):
        choice = random.choice(list(self._board.legal_moves))

        return choice