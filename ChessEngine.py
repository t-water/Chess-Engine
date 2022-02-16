import chess
from abc import ABC, abstractmethod

from EvaluationBoard import EvaluationBoard

class ChessEngine(ABC):
    def __init__(self, player_color):
        self.__player_color = player_color
        self._board = EvaluationBoard()

    def __print_board(self):
        print()
        print(self._board)
        print()

    @abstractmethod
    def _computer_move(self):
        pass

    def __player_move(self):
        legal_move_selected = False
        chosen_move = input("Please input a move:")

        while not legal_move_selected:
            try:
                self._board.push_san(chosen_move)
                legal_move_selected = True
            except ValueError:
                chosen_move = input("Please input a move:")

    def start(self):
        outcome = self._board.outcome()

        while(outcome is None):
            self.__print_board()

            is_players_turn = self.__player_color == self._board.turn

            if is_players_turn:
                self.__player_move()
            else:
                self._board.push(self._computer_move())
            
            self.__increment_turn()
            outcome = self._board.outcome()
            
        self.__print_board()
        print(outcome)
        print(outcome.result())