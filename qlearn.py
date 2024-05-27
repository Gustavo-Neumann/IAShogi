import random
import shogi
import numpy as np
import pickle
from collections import defaultdict
import os
import zlib
import iashogi

# Hyperparameters for Q-Learning
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.2  # Exploration rate
num_episodes = 1000  # Number of episodes for training
minimax_probability = 0.0  # Probability of using Minimax

# Q-Table
Q = defaultdict(float)
board = shogi.Board()

# Function to choose an action based on the epsilon-greedy policy and Minimax
def choose_action(state, legal_moves):
    if np.random.rand() < epsilon:
        return random.choice(legal_moves)
    elif np.random.rand() < minimax_probability:
        print("MINIMAX!!!")
        return iashogi.selectmove(3)
    else:
        q_values = [Q[(state, move.usi())] for move in legal_moves]
        max_q_value = max(q_values)
        max_q_actions = [move for move, q in zip(legal_moves, q_values) if q == max_q_value]
        return random.choice(max_q_actions)

# Function to update Q-Table
def update_q_table(state, action, reward, next_state, done):
    current_q = Q[(state, action)]
    max_future_q = max([Q[(next_state, move.usi())] for move in board.legal_moves], default=0)
    new_q = current_q + alpha * (reward + gamma * max_future_q * (1 - done) - current_q)
    Q[(state, action)] = new_q

# Function to save Q-Table in binary format
def save_q_table(filename):
    with open(filename, 'wb') as f:
        compressed_data = zlib.compress(pickle.dumps(dict(Q)))
        f.write(compressed_data)

# Function to load Q-Table from binary format
def load_q_table(filename):
    global Q
    with open(filename, 'rb') as f:
        compressed_data = f.read()
        Q = defaultdict(float, pickle.loads(zlib.decompress(compressed_data)))

# Function to create Q-Table file if it doesn't exist
def create_q_table_if_not_exists(filename):
    if not os.path.exists(filename):
        save_q_table(filename)
        print(f"Created new Q-Table file: {filename}")
    else:
        load_q_table(filename)
        print(f"Loaded existing Q-Table file: {filename}")

# Initialize Q-Table
create_q_table_if_not_exists('q_table.pkl')

# Training loop
def train():
    print("Treinando o modelo")
    board.reset()
    for episode in range(num_episodes):
        board.reset()
        state = board.sfen()
        while not board.is_game_over():
            legal_moves = list(board.legal_moves)
            action = choose_action(state, legal_moves)
            board.push_usi(action.usi())
            next_state = board.sfen()
            reward = 0
            done = board.is_game_over()

            if done:
                if board.is_checkmate():
                    reward = 1 if board.turn == shogi.BLACK else -1
                    print(board)
                    print(reward, episode)
                elif board.is_fourfold_repetition():
                    reward = 0.5
            update_q_table(state, action.usi(), reward, next_state, done)
            state = next_state

    # Save the trained Q-Table
    save_q_table('q_table.pkl')

# Play against the trained Q-Learning agent
def play():
    board.reset()
    while not board.is_game_over():
        if board.turn:
            # Replace this with your function for human move
            legal_moves = list(board.legal_moves)
            print("Legal moves:", [move.usi() for move in legal_moves])
            move_str = input("Enter your move (USI format): ")
            if move_str in [move.usi() for move in legal_moves]:
                board.push_usi(move_str)
            else:
                print("Invalid move. Try again.")
        else:
            state = board.sfen()
            legal_moves = list(board.legal_moves)
            action = choose_action(state, legal_moves)
            board.push_usi(action.usi())
            print(board)

    if board.is_checkmate():
        if board.turn == shogi.BLACK:
            print("Branco venceu por cheque-mate!")
        else:
            print("Preto venceu por cheque-mate!")
    elif board.is_fourfold_repetition():
        print("Empate por repetição quádrupla.")

def qlearn_vs_minimax():
    print("Qlearn vs Minimax!!!")
    board.reset()
    while not board.is_game_over():
        if board.turn:
            state = board.sfen()
            legal_moves = list(board.legal_moves)
            action = choose_action(state, legal_moves)
            board.push_usi(action.usi())
            print(board) 
        else:
           move = iashogi.selectmove(3)
           board.push(move)
           print(board)

    if board.is_checkmate():
        if board.turn == shogi.BLACK:
            print("Branco venceu por cheque-mate!")
        else:
            print("Preto venceu por cheque-mate!")
    elif board.is_fourfold_repetition():
        print("Empate por repetição quádrupla.")  

def menu():
    while True:
        print("Escolha uma opção:")
        print("1. Treinar o modelo")
        print("2. Jogar contra o agente treinado")
        print("3. Q learn contra Minimax")
        print("4. Sair")
        
        choice = input("Digite sua escolha (1/2/3): ")
        
        if choice == '1':
            train()
        elif choice == '2':
            play()
        elif choice == '3':
            qlearn_vs_minimax()
        elif choice == '4':
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == '__main__':
    menu()
