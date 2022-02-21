import chess
from ChessEngine import ChessEngine


class BruteForce(ChessEngine):
    def __init__(self, player_color):
        super().__init__(player_color)

        self.__computer_color = not player_color

        def _computer_move(self):
            pass