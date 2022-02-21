from collections import deque
from Linear_QNet import Linear_QNet
from QTrainer import QTrainer

MAX_MEMORY = 100000
BATCH_SIZE = 1000
LEARNING_RATE = 0.001
MAX_POSSIBLE_MOVES = 32 * 27

class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0.9
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = Linear_QNet(64, 256, MAX_POSSIBLE_MOVES)
        self.trainer = QTrainer(self.model, learning_rate=LEARNING_RATE, gamma=self.gamma)

    def increment_games_count(self):
        self.n_games += 1

    def get_state(self, game):
        pass

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def train_long_memory(self):
        pass

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)
    
    def get_action(self, state):
        pass