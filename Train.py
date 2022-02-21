import chess
import time
from Agent import Agent
from NeuralNetwork import NeuralNetwork

def take_step(game, agent):
    old_state = agent.get_state(game)
    final_move = agent.get_action(game, old_state)

    reward, done = game.play_step(final_move, agent.color)
    new_state = agent.get_state(game)

    agent.train_short_memory(old_state, final_move, reward, new_state, done)

    agent.remember(old_state, final_move, reward, new_state, done)

    if done:
        print("DONE!")
        game.reset()
        agent.increment_games_count()
        agent.train_long_memory()

        if reward > 0.5:
            agent.model.save()
    
    return done

def train():
    white_agent = Agent(chess.WHITE)
    black_agent = Agent(chess.BLACK)
    game = NeuralNetwork()

    game_finished = False
    current_agent = white_agent

    while True:
        game_finished = take_step(game, current_agent)

        if game_finished:
            current_agent = white_agent
            game_finished = False
        else:
            current_agent = black_agent if current_agent == white_agent else white_agent

train()