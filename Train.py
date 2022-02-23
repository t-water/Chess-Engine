
import chess
import torch
import random
from Agent import Agent
from NeuralNetwork import NeuralNetwork
from RandomEngine import RandomEngine

def take_step(game, agent):
    old_state = agent.get_state(game)
    final_move = agent.get_action(game, old_state)

    reward, done = game.play_step(final_move, agent.color)
    new_state = agent.get_state(game)         
    
    return old_state, final_move, reward, new_state, done

def train_short_memory(agent, old_state, final_move, reward, new_state, done):
    agent.train_short_memory(old_state, final_move, reward, new_state, done)
    agent.remember(old_state, final_move, reward, new_state, done)  

def finish_game(game, agent):
    game.reset()
    agent.increment_games_count()
    agent.train_long_memory()

    if agent.n_games % 100 == 0:
        agent.model.save()

def train():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    wins = 0
    losses = 0
    draws = 0

    white_agent = Agent(chess.WHITE, device)
    game = NeuralNetwork()

    game_finished = False

    while True:
        old_state, final_move, reward, new_state, game_finished = take_step(game, white_agent)
        
        if not game_finished:
            num_legal_moves = len(list(game.board.legal_moves))
            action = [0 for _ in range(num_legal_moves)]
            move = random.randint(0, num_legal_moves-1)
            action[move] = 1

            reward, game_finished = game.play_step(action, chess.BLACK)

            if reward > 0.5:
                reward = 0 if reward == 1 else 1
        
        train_short_memory(white_agent, old_state, final_move, reward, new_state, game_finished)

        if game_finished:
            if reward > 0.5:
                wins += 1
            elif reward < 0.5:
                losses += 1
            else:
                draws += 1

            print("---------------------------------------------")
            print()
            print(game.board)
            print()
            print(f"OUTCOME: {game.board.outcome().termination} REWARD: {reward}")
            print(f"{wins}-{losses}-{draws} ({wins + losses + draws})")
            finish_game(game, white_agent)

train()