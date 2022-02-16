import chess

class EvaluationBoard(chess.Board):
    all_squares = chess.SquareSet(chess.BB_ALL)
    center_squares = chess.SquareSet(chess.BB_CENTER)
    back_rank_squares = chess.SquareSet(chess.BB_BACKRANKS)

    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9
    }

    center_square_value = 0.25
    development_value = 0.1
    checkmate_value = 1000

    def __init__(self):
        super().__init__()
    
    def __material_advantage(self):
        total = 0

        for square in EvaluationBoard.all_squares:
            square_piece = self.piece_at(square)
            
            if square_piece:
                square_piece_value = EvaluationBoard.piece_values.get(square_piece.piece_type, 0)

                if square_piece.color == chess.WHITE:
                    total += square_piece_value
                else:
                    total -= square_piece_value
        
        return total

    def __center_square_advantage(self):
        total = 0

        for square in EvaluationBoard.center_squares:
            white_attacking_pieces = self.attackers(chess.WHITE, square)
            black_attacking_pieces = self.attackers(chess.BLACK, square)

            total += len(white_attacking_pieces) * EvaluationBoard.center_square_value
            total -= len(black_attacking_pieces) * EvaluationBoard.center_square_value

        return total
    
    def __development_advantage(self):
        total = 0

        for square in EvaluationBoard.back_rank_squares:
            square_piece = self.piece_at(square)

            if square_piece == chess.BISHOP or square_piece == chess.KNIGHT:
                total += -EvaluationBoard.development_value if square_piece.color == chess.WHITE else EvaluationBoard.development_value

        return total
    
    def __game_is_terminated(self):
        return self.outcome() is None

    def __termination_value(self):
        is_whites_turn = self.turn == chess.WHITE

        if self.is_checkmate():
            return -EvaluationBoard.checkmate_value if is_whites_turn else EvaluationBoard.checkmate_value
        
        return 0
    
    def evaluate_position(self):
        evaluation = 0

        if self.__game_is_terminated():
            self.__termination_value()

        evaluation += self.__material_advantage()
        evaluation += self.__center_square_advantage()
        evaluation += self.__development_advantage()
        
        return evaluation