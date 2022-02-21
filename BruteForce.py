import chess
from ChessEngine import ChessEngine


class BruteForce(ChessEngine):
    def __init__(self, player_color):
        super().__init__(player_color)

        self.__computer_color = not player_color
    
    def __get_legal_moves(self, game_state):
        return list(game_state.legal_moves)

    def __min_value(self, game_state, ply):
        legal_moves = self.__get_legal_moves(game_state)

        if ply <= 0 or len(legal_moves) == 0:
            return (None, self.board.evaluate_position())
        
        best_move = None
        best_move_value = None

        for move in legal_moves:
            game_state.push(move)
            future_best_move, move_value = self.__max_value(game_state, ply-1)
            game_state.pop()

            if not best_move or move_value < best_move_value:
                best_move = move
                best_move_value = move_value
        
        return (best_move, best_move_value)

    def __max_value(self, game_state, ply):
        legal_moves = self.__get_legal_moves(game_state)

        if ply <= 0 or len(legal_moves) == 0:
            return (None, self.board.evaluate_position())
        
        best_move = None
        best_move_value = None

        for move in legal_moves:
            game_state.push(move)
            future_best_move, move_value = self.__min_value(game_state, ply-1)
            game_state.pop()

            if not best_move or move_value > best_move_value:
                best_move = move
                best_move_value = move_value
        
        return (best_move, best_move_value)
    
    def __search(self, ply):
        if self.__computer_color == chess.WHITE:
            return self.__max_value(self.board, ply)[0]
        else:
            return self.__min_value(self.board, ply)[0]
    
    def _computer_move(self):
        return self.__search(3)