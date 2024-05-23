import random
import shogi
import numpy as np

board = shogi.Board()


# Função para obter o estado do jogo
def get_state(board):
    return board.sfen()


# Função para obter as ações possíveis
def get_actions(board):
    return [move.usi() for move in board.legal_moves]


# Inicialização da tabela Q
Q = {}


# Função para atualizar a tabela Q
def update_q_table(Q, state, action, reward, next_state, alpha=0.1, gamma=0.9):
    state_str = str(state)
    next_state_str = str(next_state)
    if state_str not in Q:
        Q[state_str] = {a: 0 for a in get_actions(board)}
    if next_state_str not in Q:
        Q[next_state_str] = {a: 0 for a in get_actions(board)}

    current_q = Q[state_str].get(action, 0)
    max_next_q = max(Q[next_state_str].values(), default=0)
    Q[state_str][action] = current_q + alpha * (reward + gamma * max_next_q -
                                                current_q)


# Função para selecionar a ação
def select_action(Q, state, epsilon=0.1):
    state_str = str(state)
    if state_str not in Q or np.random.rand() < epsilon:
        return random.choice(get_actions(board))
    else:
        return max(Q[state_str], key=Q[state_str].get)


# Função para calcular a recompensa
def get_reward(board):
    if board.is_checkmate():
        return 1000 if board.turn else -1000
    elif board.is_game_over():
        return 0
    else:
        return 1


# Função para treinar o agente
def train_agent(board, episodes=1000, alpha=0.1, gamma=0.9, epsilon=0.1):
    for episode in range(episodes):
        board.reset()
        state = get_state(board)

        while not board.is_game_over():
            action = select_action(Q, state, epsilon)
            board.push_usi(action)
            next_state = get_state(board)
            reward = get_reward(board)

            update_q_table(Q, state, action, reward, next_state, alpha, gamma)

            state = next_state


# Função para avaliar os agentes
def evaluate_agents(episodes=100):
    q_learning_wins = 0
    minimax_wins = 0
    draws = 0

    for episode in range(episodes):
        board.reset()

        while not board.is_game_over():
            if board.turn:
                action = select_action(Q, get_state(board), epsilon=0)
            else:
                action = selectmove(3)

            board.push_usi(action)

        if board.is_checkmate():
            if board.turn:
                minimax_wins += 1
            else:
                q_learning_wins += 1
        else:
            draws += 1

    print(f"Q-Learning Wins: {q_learning_wins}")
    print(f"Minimax Wins: {minimax_wins}")
    print(f"Draws: {draws}")


# Funções auxiliares do Minimax
def avalia_board():
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
    if board.is_game_over():
        return 0

    peao_branco = 0
    lanca_branca = 0
    cavalo_branco = 0
    general_prata_branco = 0
    general_ouro_branco = 0
    bispo_branco = 0
    torre_branca = 0
    rei_branco = 0

    peao_preto = 0
    lanca_preta = 0
    cavalo_preto = 0
    general_prata_preto = 0
    general_ouro_preto = 0
    bispo_preto = 0
    torre_preta = 0
    rei_preto = 0

    for piece in board.pieces:
        if board.turn == shogi.WHITE:
            if piece == shogi.PAWN:
                peao_branco += 1
            elif piece == shogi.LANCE:
                lanca_branca += 1
            elif piece == shogi.KNIGHT:
                cavalo_branco += 1
            elif piece == shogi.SILVER:
                general_prata_branco += 1
            elif piece == shogi.GOLD:
                general_ouro_branco += 1
            elif piece == shogi.BISHOP:
                bispo_branco += 1
            elif piece == shogi.ROOK:
                torre_branca += 1
            elif piece == shogi.KING:
                rei_branco += 1
        if board.turn == shogi.BLACK:
            if piece == shogi.PAWN:
                peao_preto += 1
            elif piece == shogi.LANCE:
                lanca_preta += 1
            elif piece == shogi.KNIGHT:
                cavalo_preto += 1
            elif piece == shogi.SILVER:
                general_prata_preto += 1
            elif piece == shogi.GOLD:
                general_ouro_preto += 1
            elif piece == shogi.BISHOP:
                bispo_preto += 1
            elif piece == shogi.ROOK:
                torre_preta += 1
            elif piece == shogi.KING:
                rei_preto += 1

    material = 100 * (peao_branco - peao_preto) + 850 * (
        bispo_branco -
        bispo_preto) + 950 * (torre_branca - torre_preta) + 550 * (
            general_ouro_branco - general_ouro_preto
        ) + 450 * (general_prata_branco - general_prata_preto) + 320 * (
            cavalo_branco - cavalo_preto) + 300 * (lanca_branca - lanca_preta)

    avaliacao = material  # + outras avaliações se necessário
    if board.turn:
        return avaliacao
    else:
        return -avaliacao


def alphabeta(alpha, beta, depthleft):
    bestscore = -9999
    if (depthleft == 0):
        return quiesce(alpha, beta)
    for move in board.legal_moves:
        board.push(move)
        score = -alphabeta(-beta, -alpha, depthleft - 1)
        board.pop()
        if (score >= beta):
            return score
        if (score > bestscore):
            bestscore = score
        if (score > alpha):
            alpha = score
    return bestscore


def is_capture(board, move):
    piece_at_destination = board.piece_at(move.to_square)
    return piece_at_destination is not None and piece_at_destination.color != board.turn


def quiesce(alpha, beta):
    stand_pat = avalia_board()
    if (stand_pat >= beta):
        return beta
    if (alpha < stand_pat):
        alpha = stand_pat

    for move in board.legal_moves:
        if is_capture(board, move):
            board.push(move)
            score = -quiesce(-beta, -alpha)
            board.pop()

            if (score >= beta):
                return beta
            if (score > alpha):
                alpha = score
    return alpha


def selectmove(depth):
    bestMove = shogi.Move.null()
    bestValue = -99999
    alpha = -100000
    beta = 100000
    for move in board.legal_moves:
        board.push(move)
        boardValue = -alphabeta(-beta, -alpha, depth - 1)
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
        if (boardValue > alpha):
            alpha = boardValue
        board.pop()
    return bestMove


# Treinamento e avaliação
train_agent(board)
evaluate_agents()
