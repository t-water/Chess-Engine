from ChessEngine import ChessEngine
import random


class BruteForce(ChessEngine):
    def __init__(self, player_color):
        super().__init__(player_color)

        self.__position_evaluations = {}

    def __get_average_evaluation(self, game_state, ply):
        key = game_state.board_fen()
        average_evaluation = 0
        legal_moves = list(game_state.legal_moves)

        if key in self.__position_evaluations:
            return self.__position_evaluations[key]

        current_position_evaluation = game_state.evaluate_position()

        if ply == 0 or len(legal_moves) == 0:
            average_evaluation = current_position_evaluation
        else:
            position_evaluation = current_position_evaluation
            total_evaluation = 0
            
            for move in legal_moves:
                game_state.push(move)
                total_evaluation += self.__get_average_evaluation(game_state, ply-1)
                game_state.pop()
            
            average_evaluation = (position_evaluation + (total_evaluation / len(legal_moves))) / 2

        self.__position_evaluations[key] = average_evaluation

        return average_evaluation
    
    def __search(self, game_state, ply):
        best_move = None
        best_move_advantage = None

        for move in game_state.legal_moves:
            game_state.push(move)
            move_advantage = self.__get_average_evaluation(game_state, ply)
            game_state.pop()

            if best_move is None or move_advantage > best_move_advantage:
                best_move = move
                best_move_advantage = move_advantage
    
        return best_move

    
    def _computer_move(self):
        return self.__search(self._board, 2)
            