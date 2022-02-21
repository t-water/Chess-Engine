from EvaluationBoard import EvaluationBoard

class NeuralNetwork:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.board = EvaluationBoard()
    
    def play_step(self, action, color):
        self._move(action)

        game_over = False
        reward = 0

        if self.board.outcome():
            game_over = True

            if self.board.is_checkmate():
                reward = -1 if self.board.turn == color else 1
            else:
                reward = 0.5
        
        return reward, game_over

    def _move(self, action):
        legal_moves = self.board.get_legal_moves()

        selected_move_index = action.index(1)
        selected_move = legal_moves[selected_move_index]
        
        self.board.push(selected_move)

    def __str__(self):
        return str(self.board)