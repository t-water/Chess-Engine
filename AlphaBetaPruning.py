from math import inf
import chess
from ChessEngine import ChessEngine


class AlphaBetaPruning(ChessEngine):
    def __init__(self, player_color):
        super().__init__(player_color)

        self.__computer_color = not player_color
        self.__max_memo = {}
        self.__min_memo = {}
    
    def __get_key(self, game_state):
        return game_state.board_fen()
    
    def __get_legal_moves(self, game_state):
        legal_moves = list(game_state.legal_moves)

        legal_moves.sort(key = lambda move : 0 if game_state.is_capture(move) else 1)

        return legal_moves 

    def __min_value(self, game_state, ply, alpha, beta):
        legal_moves = self.__get_legal_moves(game_state)
        key = self.__get_key(game_state)

        if key in self.__min_memo:
            return self.__min_memo[key]

        if ply <= 0 or len(legal_moves) == 0:
            return (None, self._board.evaluate_position())
        
        best_move = None
        best_move_value = None

        for move in legal_moves:
            game_state.push(move)
            future_best_move, move_value = self.__max_value(game_state, ply-1, alpha, beta)
            game_state.pop()

            if not best_move or move_value < best_move_value:
                best_move = move
                best_move_value = move_value
                beta = min(beta, move_value)
            
            if best_move_value <= alpha:
                self.__min_memo[key] = (best_move, best_move_value)
                return (best_move, best_move_value)
        
        self.__min_memo[key] = (best_move, best_move_value)
        return (best_move, best_move_value)

    def __max_value(self, game_state, ply, alpha, beta):
        legal_moves = self.__get_legal_moves(game_state)
        key = self.__get_key(game_state)

        if key in self.__max_memo:
            return self.__max_memo[key]

        if ply <= 0 or len(legal_moves) == 0:
            return (None, self._board.evaluate_position())
        
        best_move = None
        best_move_value = None

        for move in legal_moves:
            game_state.push(move)
            future_best_move, move_value = self.__min_value(game_state, ply-1, alpha, beta)
            game_state.pop()

            if not best_move or move_value > best_move_value:
                best_move = move
                best_move_value = move_value
                alpha = max(alpha, move_value)
            
            if best_move_value >= beta:
                self.__max_memo[key] = (best_move, best_move_value)
                return (best_move, best_move_value)
        
        self.__max_memo[key] = (best_move, best_move_value)
        return (best_move, best_move_value)
    
    def __search(self, ply):
        if self.__computer_color == chess.WHITE:
            return self.__max_value(self._board, ply, -inf, inf)[0]
        else:
            return self.__min_value(self._board, ply, -inf, inf)[0]
    
    def _computer_move(self):
        return self.__search(4)
            