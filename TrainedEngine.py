from Agent import Agent
from ChessEngine import ChessEngine

class TrainedEngine(ChessEngine):
    def __init__(self, player_color):
        super().__init__(player_color)

        self.agent = Agent(not player_color)
    
    def _computer_move(self):
        old_state = self.agent.get_state(self)
        final_move = self.agent.get_action(self, old_state)

        legal_moves = self.board.get_legal_moves()

        selected_move_index = final_move.index(1)
        selected_move = legal_moves[selected_move_index]

        return selected_move