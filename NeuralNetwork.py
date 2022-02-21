import chess
from EvaluationBoard import EvaluationBoard

class NeuralNetwork:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.board = EvaluationBoard()
    
    def play_step(self, action):
        pass

    