import random
import shogi

board = shogi.Board()


def move_piece(board):
    while True:  # Continua até que um movimento válido seja feito
        print("Movimentos legais possíveis:", [move.usi() for move in board.legal_moves])
        move_str = input("Por favor, digite seu movimento (formato USI): ")
        try:
            if any(move_str == move.usi() for move in board.legal_moves):
                board.push_usi(move_str)
                break
            else:
                print("Moviemento invalido tente novamente")
        except ValueError:
            print("Formato de movimento inválido. Por favor, use o formato USI e tente novamente.")


#  Pontuação das peças de acordo com a posição


peao_value = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    10, 20, 20, -10, -10, 20, 20, 10, 10,
    10, -5, -10, 5, 5, -10, -5, 10, 10,
    5, 5, 10, 25, 25, 10, 5, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10, 10,
    20, 20, 30, 40, 40, 30, 20, 20, 20,
    50, 50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0
]

lanca_value = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    10, 20, 25, 30, 30, 25, 20, 10, 10,
    10, 20, 25, 30, 30, 25, 20, 10, 10,
    10, 20, 25, 30, 30, 25, 20, 10, 10,
    10, 20, 25, 30, 30, 25, 20, 10, 10,
    10, 20, 25, 30, 30, 25, 20, 10, 10,
    10, 20, 25, 30, 30, 25, 20, 10, 10,
    10, 20, 25, 30, 30, 25, 20, 10, 10,
    0, 0, 0, 0, 0, 0, 0, 0, 0
]

cavalo_value = [
    -50, -40, -30, -20, -20, -30, -40, -50, -60,
    -30, -10, 5, 10, 10, 5, -10, -30, -40,
    -20, 10, 20, 25, 25, 20, 10, -20, -30,
    -10, 15, 25, 30, 30, 25, 15, -10, -20,
    -10, 15, 25, 30, 30, 25, 15, -10, -20,
    -20, 10, 20, 25, 25, 20, 10, -20, -30,
    -30, -10, 5, 10, 10, 5, -10, -30, -40,
    -50, -40, -30, -20, -20, -30, -40, -50, -60,
    -60, -50, -40, -30, -30, -40, -50, -60, -70
]

generais_de_ouro_value = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    10, 15, 20, 20, 20, 20, 20, 15, 10,
    10, 15, 20, 20, 20, 20, 20, 15, 10,
    10, 15, 20, 20, 20, 20, 20, 15, 10,
    10, 15, 20, 20, 20, 20, 20, 15, 10,
    10, 15, 20, 20, 20, 20, 20, 15, 10,
    10, 15, 20, 20, 20, 20, 20, 15, 10,
    10, 15, 20, 20, 20, 20, 20, 15, 10,
    0, 0, 0, 0, 0, 0, 0, 0, 0
]

generais_de_prata_value = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    10, 15, 20, 25, 25, 20, 15, 10, 10,
    10, 15, 20, 25, 25, 20, 15, 10, 10,
    10, 15, 20, 25, 25, 20, 15, 10, 10,
    10, 15, 20, 25, 25, 20, 15, 10, 10,
    10, 15, 20, 25, 25, 20, 15, 10, 10,
    10, 15, 20, 25, 25, 20, 15, 10, 10,
    10, 15, 20, 25, 25, 20, 15, 10, 10,
    0, 0, 0, 0, 0, 0, 0, 0, 0
]

bispo_value = [
    -20, -10, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 0, 5, -10,
    -10, 10, 15, 20, 20, 15, 10, 0, -10,
    -10, 0, 20, 25, 25, 20, 5, 5, -10,
    -10, 0, 20, 25, 25, 20, 5, 5, -10,
    -10, 10, 15, 20, 20, 15, 10, 0, -10,
    -10, 5, 0, 5, 5, 0, 5, 5, -10,
    -20, -10, -10, -10, -10, -10, -10, -10, -20
]

torre_value = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 15, 20, 20, 15, 10, 5, 5,
    5, 10, 15, 20, 20, 15, 10, 5, 5,
    5, 10, 15, 20, 20, 15, 10, 5, 5,
    5, 10, 15, 20, 20, 15, 10, 5, 5,
    5, 10, 15, 20, 20, 15, 10, 5, 5,
    5, 10, 15, 20, 20, 15, 10, 5, 5,
    5, 10, 15, 20, 20, 15, 10, 5, 5,
    0, 0, 0, 5, 5, 0, 0, 0, 0
]

# Para o rei, garantir a segurança melhorando as posições defensivas
rei_value = [
    20, 30, 40, 50, 50, 40, 30, 20, 10,
    20, 30, 40, 50, 50, 40, 30, 20, 10,
    20, 30, 40, 50, 50, 40, 30, 20, 10,
    20, 30, 40, 50, 50, 40, 30, 20, 10,
    20, 30, 40, 50, 50, 40, 30, 20, 10,
    20, 30, 40, 50, 50, 40, 30, 20, 10,
    20, 30, 40, 50, 50, 40, 30, 20, 10,
    20, 30, 40, 50, 50, 40, 30, 20, 10,
    20, 30, 40, 50, 50, 40, 30, 20, 10
]


def avalia_board():
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
    if board.is_game_over():
        return 0


# '''Número de peças que estão no tabuleiro
# - utilizado pra fazer o calculo material da diferença de peças suas e do adversario


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

    piece = shogi.Piece
    
    # Contar peças brancas
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

    # Contar peças pretas
    for piece in board.pieces:
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

# 1 Rei
# 1 Torre
# 1 Bispo
# 2 Generais de Ouro
# 2 Generais de Prata
# 2 Cavalos
# 2 Lanças
# 9 Peões
    material = 100 * (peao_branco - peao_preto) + 850 * (bispo_branco - bispo_preto) + 950 * (torre_branca - torre_preta) + 550 * (general_ouro_branco - general_ouro_preto) + 450 * (general_prata_branco - general_prata_preto) + 320 * (cavalo_branco - cavalo_preto) + 300 * (lanca_branca - lanca_preta)


    peaosq = sum([peao_value[i] for i in range(peao_branco)])
    peaosq = peaosq + sum([-peao_value[i]
                           for i in range(peao_preto)])
    
    cavalosq = sum([cavalo_value[i] for i in range(cavalo_branco)])
    cavalosq = cavalosq + sum([-cavalo_value[i]
                               for i in range(cavalo_preto)])
    
    bisposq = sum([bispo_value[i] for i in range(bispo_branco)])
    bisposq = bisposq + sum([-bispo_value[i]
                               for i in range(bispo_preto)])
    
    torresq = sum([torre_value[i] for i in range(torre_branca)])
    torresq = torresq + sum([-torre_value[i]
                           for i in range(torre_preta)])
    
    goldsq = sum([generais_de_ouro_value[i] for i in range(general_ouro_branco)])
    goldsq = goldsq + sum([-generais_de_ouro_value[i]
                             for i in range(general_ouro_preto)])
    
    silversq = sum([generais_de_prata_value[i] for i in range(general_prata_branco)])
    silversq = silversq + sum([-generais_de_prata_value[i]
                             for i in range(general_prata_preto)])
    
    reisq = sum([rei_value[i] for i in range(rei_branco)])
    reisq = reisq + sum([-rei_value[i]
                           for i in range(rei_preto)])

    avaliacao = material + peaosq + cavalosq + bisposq + torresq + goldsq + reisq + silversq
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


def quiesce( alpha, beta ):
    stand_pat = avalia_board()
    if( stand_pat >= beta ):
        return beta
    if( alpha < stand_pat ):
        alpha = stand_pat

    for move in board.legal_moves:
        if is_capture(board, move):
            board.push(move)
            score = -quiesce( -beta, -alpha )
            board.pop()

            if( score >= beta ):
                return beta
            if( score > alpha ):
                alpha = score
    return alpha


def selectmove(depth):
        movehistory =[]
        bestMove = shogi.Move.null()
        bestValue = -99999
        alpha = -100000
        beta = 100000
        for move in board.legal_moves:
            board.push(move)
            boardValue = -alphabeta(-beta, -alpha, depth-1)
            if boardValue > bestValue:
                bestValue = boardValue
                bestMove = move
            if( boardValue > alpha ):
                alpha = boardValue
            board.pop()
        movehistory.append(bestMove)
        return bestMove


def random_move(board):
    legal_moves = list(board.legal_moves)
    if legal_moves:  # Verifica se há movimentos legais disponíveis
        return random.choice(legal_moves)
    else:
        return None 

# while not board.is_game_over():
#     if board.turn:
#         # Funcao para jogar contra a IA
#         # move_piece(board)

#         # Funcao que joga movimentos aleatorios
#         board.push(random_move(board))
#         print(board)
#     else:
#         # IA Jogando
#         move = selectmove(3)
#         board.push(move) 
#         print(board)
        

# board

# if board.is_checkmate():
#     if board.turn == shogi.BLACK:
#         print("Branco venceu por cheque-mate!")
#     else:
#         print("Preto venceu por cheque-mate!")
# elif board.is_fourfold_repetition():
#     print("Empate por repetição quádrupla.")

# board.reset()