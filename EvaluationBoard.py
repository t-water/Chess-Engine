import chess

class EvaluationBoard(chess.Board):
    all_squares = chess.SquareSet(chess.BB_ALL)
    center_squares = chess.SquareSet(chess.BB_CENTER)

    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }

    center_square_value = 0.05

    def __init__(self):
        super().__init__()
    
    def __material_advantage(self):
        total = 0

        for square in EvaluationBoard.all_squares:
            square_piece = self.piece_at(square)
            square_piece_value = EvaluationBoard.piece_values[square_piece.piece_type]

            if square_piece and square_piece.color == self.turn:
                total += square_piece_value
            else:
                total -= square_piece_value
        
        return total

    def __center_square_advantage(self):
        pass
         
    
    def evaluate_position(self):
        evaluation = 0
        is_whites_turn = self.turn == chess.WHITE

        if self.is_checkmate():
            return -100 if is_whites_turn else 100 

        evaluation += self.__material_advantage()
        
        return evaluation