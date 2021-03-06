from collections import deque
import random

from Linear_QNet import Linear_QNet
from QTrainer import QTrainer
import torch

MAX_MEMORY = 100000
BATCH_SIZE = 1000
LEARNING_RATE = 0.2
MAX_POSSIBLE_MOVES = 64 * 64

class Agent:
    def __init__(self, color, device):
        self.color = color
        self.device = device
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0.9
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = Linear_QNet(64, 256, MAX_POSSIBLE_MOVES).to(self.device)
        self.trainer = QTrainer(self.model, LEARNING_RATE, self.gamma, self.device)

        # file_name='model.pth'
        # model_folder_path = './model'
        # file_name = os.path.join(model_folder_path, file_name)
        # self.model.load_state_dict(torch.load(file_name))
        # self.model.eval()

    def increment_games_count(self):
        self.n_games += 1

    def get_state(self, game):
        return game.board.state

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory
        
        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)
    
    def get_action(self, game, state):
        self.epsilon = 10000 - self.n_games
        
        final_move = [0 for _ in range(MAX_POSSIBLE_MOVES)]
        move = 0

        if random.randint(0, 50000) < self.epsilon:
            legal_moves = game.board.get_legal_moves()
            random_legal_move = random.choice(legal_moves)
            move = random_legal_move.from_square * 64 + random_legal_move.to_square
        else:
            state_tensor = torch.tensor(state, dtype=torch.float).to(self.device)
            prediction = self.model(state_tensor)
            move = torch.argmax(prediction).item()

        final_move[move] = 1

        return final_move