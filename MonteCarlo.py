import random
import chess

class TreeNode:
    def __init__(self, fen, parent):
        self.board = chess.Board(fen)
        self.parent = parent
        self.legal_moves = list(self.board.legal_moves)
        self.children = {}
        self.wins = 0
        self.playouts = 0
    
    def select(self):
        chosen_move = random.choice(self.legal_moves)
        self.board.push(chosen_move)
        key = self.board.fen()

        if key in self.children:
            child_node = self.children[key]
            self.board.pop()

            child_node.select()
        else:
            child_node = TreeNode(key, self)
            self.children[key] = child_node

            self.board.pop()

            child_node.expand()
    
    def expand(self):
        game = chess.Board(self.board.fen())

        while not game.outcome():
            chosen_move = random.choice(list(game.legal_moves))
            game.push(chosen_move)

        winner = game.outcome().winner
        
        return self.propagate(winner)
        
    def propagate(self, winner):
        self.playouts += 1

        if winner == self.board.turn:
            self.wins += 1
        elif not winner:
            self.wins += 0.5

        if self.parent:
            self.parent.propagate(winner)

def main():
    starting_position = TreeNode(chess.Board().fen(), None)

    for i in range(800):
        starting_position.select()
        print(f"{starting_position.wins}/{starting_position.playouts}")

    # for child in starting_position.children.values():
    #     print(f"{child.board.fen()}: {child.wins}/{child.playouts}")

main()