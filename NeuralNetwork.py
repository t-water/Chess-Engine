from EvaluationBoard import EvaluationBoard
import chess

class NeuralNetwork:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.board = EvaluationBoard()        
    
    def play_step(self, action, color):
        self.board.move(action)

        game_over = False
        reward = 0

        if self.board.outcome():
            game_over = True

            if self.board.is_checkmate():
                reward = -1 if self.board.turn == color else 1
            else:
                reward = 0.5
        
        return reward, game_over

    def __str__(self):
        return str(self.board)