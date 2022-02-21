import chess
from abc import ABC, abstractmethod

from EvaluationBoard import EvaluationBoard

class ChessEngine(ABC):
    def __init__(self, player_color):
        self.__player_color = player_color
        self.board = EvaluationBoard()

    def __printboard(self):
        print()
        print(self.board)
        print()

    @abstractmethod
    def _computer_move(self):
        pass

    def __player_move(self):
        legal_move_selected = False
        chosen_move = input("Please input a move:")

        while not legal_move_selected:
            try:
                self.board.push_san(chosen_move)
                legal_move_selected = True
            except ValueError:
                chosen_move = input("Please input a move:")

    def start(self):
        outcome = self.board.outcome()

        while(outcome is None):
            self.__printboard()

            is_players_turn = self.__player_color == self.board.turn

            if is_players_turn:
                self.__player_move()
            else:
                self.board.push(self._computer_move())
            
            outcome = self.board.outcome()
            
        self.__printboard()
        print(outcome)
        print(outcome.result())