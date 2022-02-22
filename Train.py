import chess
from Agent import Agent
from NeuralNetwork import NeuralNetwork

def finish_game(agent):
    agent.increment_games_count()
    agent.train_long_memory()
    agent.model.save()    

def train_memory(agent, old_state, final_move, reward, new_state, done):
    agent.train_short_memory(old_state, final_move, reward, new_state, done)
    agent.remember(old_state, final_move, reward, new_state, done)

def take_step(game, agent):
    old_state = agent.get_state(game)
    final_move = agent.get_action(game, old_state)

    reward, done = game.play_step(final_move, agent.color)
    new_state = agent.get_state(game)
        
    return old_state, final_move, reward, new_state, done

def train():
    white_agent = Agent(chess.WHITE)
    black_agent = Agent(chess.BLACK)
    game = NeuralNetwork()

    game_finished = False
    current_color = chess.WHITE

    while True:
        current_agent = white_agent if current_color == chess.WHITE else black_agent

        old_state, final_move, reward, new_state, done = take_step(game, current_agent)
        game_finished = done

        train_memory(white_agent, old_state, final_move, reward, new_state, done)
        train_memory(black_agent, old_state, final_move, reward, new_state, done)

        if game_finished:
            game.reset()
            
            finish_game(white_agent)
            finish_game(black_agent)

            current_color = chess.WHITE
            game_finished = False
        else:
            current_color = not current_color

train()