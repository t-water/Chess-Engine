from Agent import Agent
from NeuralNetwork import NeuralNetwork

def train():
    agent = Agent()
    game = NeuralNetwork()

    while True:
        old_state = agent.get_state(game)
        final_move = agent.get_action(old_state)
        total_score = 0

        reward, done, score = game.play_step(final_move)
        new_state = agent.get_state(game)

        agent.train_short_memory(old_state, final_move, reward, new_state, done)

        agent.remember(old_state, final_move, reward, new_state, done)

        if done:
            game.reset()
            agent.increment_games_count()
            agent.train_long_memory()

            total_score += score

train()