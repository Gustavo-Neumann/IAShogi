import random
import shogi


board = shogi.Board()

def check_move(move):
    legal_moves = list(board.legal_moves)
    if move in legal_moves:
        return move
    else:
        print("Esses são os movimentos possiveis:", legal_moves)
        input("Movimento inválido, por favor digite novamente: ")
        return move

def move_piece(move):
    check_move(move)
    board.push_usi(move)

#  Pontuação das peças de acordo com a posição


rei_value = [
    20, 30, 50, 90, 90, 50, 30, 20, 10,
    20, 30, 50, 90, 90, 50, 30, 20, 10,
    20, 30, 50, 90, 90, 50, 30, 20, 10,
    20, 30, 50, 90, 90, 50, 30, 20, 10,
    20, 30, 50, 90, 90, 50, 30, 20, 10,
    20, 30, 50, 90, 90, 50, 30, 20, 10,
    20, 30, 50, 90, 90, 50, 30, 20, 10,
    20, 30, 50, 90, 90, 50, 30, 20, 10,
    20, 30, 50, 90, 90, 50, 30, 20, 10
]

torre_value = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, 10, 10, 10, 10, 10, 5,
    -5, 0, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, 0, -5,
    0, 0, 0, 5, 5, 0, 0, 0, 0
]

bispo_value = [
    -20, -10, -10, -10, -10, -10, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 10, 10, 10, 5, 0, -10,
    -10, 5, 5, 10, 10, 10, 5, 5, -10,
    -10, 0, 10, 10, 10, 10, 10, 0, -10,
    -10, 10, 10, 10, 10, 10, 10, 10, -10,
    -10, 5, 0, 0, 0, 0, 0, 5, -10,
    -20, -10, -10, -10, -10, -10, -10, -10, -20
]

generais_de_ouro_value = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 5, 10, 10, 10, 10, 10, 5, 0,
    0, 5, 10, 10, 10, 10, 10, 5, 0,
    0, 5, 10, 10, 10, 10, 10, 5, 0,
    0, 5, 10, 10, 10, 10, 10, 5, 0,
    0, 5, 10, 10, 10, 10, 10, 5, 0,
    0, 5, 10, 10, 10, 10, 10, 5, 0,
    0, 5, 10, 10, 10, 10, 10, 5, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0
]

generais_de_prata_value = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 5, 10, 10, 10, 10, 10, 5, 0,
    0, 5, 10, 10, 10, 10, 10, 5, 0,
    0, 5, 10, 10, 10, 10, 10, 5, 0,
    0, 5, 10, 10, 10, 10, 10, 5, 0,
    0, 5, 10, 10, 10, 10, 10, 5, 0,
    0, 5, 10, 10, 10, 10, 10, 5, 0,
    0, 5, 10, 10, 10, 10, 10, 5, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

cavalo_value = [
    -50, -40, -30, -20, -20, -30, -40, -50, -60,
    -40, -20, 0, 0, 0, 0, -20, -40, -50,
    -30, 0, 10, 15, 15, 10, 0, -30, -40,
    -20, 5, 15, 20, 20, 15, 5, -20, -30,
    -20, 5, 15, 20, 20, 15, 5, -20, -30,
    -30, 0, 10, 15, 15, 10, 0, -30, -40,
    -40, -20, 0, 5, 5, 0, -20, -40, -50,
    -50, -40, -30, -20, -20, -30, -40, -50, -60,
    -60, -50, -40, -30, -30, -40, -50, -60, -70
]

lanca_value = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 15, 20, 20, 15, 10, 5, 5,
    5, 10, 15, 20, 20, 15, 10, 5, 5,
    5, 10, 15, 20, 20, 15, 10, 5, 5,
    5, 10, 15, 20, 20, 15, 10, 5, 5,
    5, 10, 15, 20, 20, 15, 10, 5, 5,
    5, 10, 15, 20, 20, 15, 10, 5, 5,
    5, 10, 15, 20, 20, 15, 10, 5, 5,
    0, 0, 0, 0, 0, 0, 0, 0, 0
]

peao_value = [
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5, 5,
    5, -5, -10, 0, 0, -10, -5, 5, 5,
    0, 0, 0, 20, 20, 0, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0
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
# - número de peao branco, peao preto, torre branca, torre preta
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
       


#    Calculo Material:
# - Pra cada uma das peças, pega o valor da posição que ela se encontra e cruza com a tabela de peças
# - No mesmo calculo ele usa mirror para calcular o valor referente as peças pretas (square mirror)

# Valor total é o valor material mais o valor de numero de peças
# negativo (adversario)
# Positivo (voce)

# Min Max:
# Minima chance de perder (quando calcula as suas jogadas baseadas na do adversario)
# Maxima chance de ganhar (baseado nas suas jogadas para ganhar)'''
# 1 Rei
#1 Torre
#1 Bispo
#2 Generais de Ouro
#2 Generais de Prata
#2 Cavalos
#2 Lanças
#9 Peões
    material = 0 * (peao_branco - peao_preto) +  800 * (bispo_branco - bispo_preto) + 900 * (torre_branca - torre_preta) + 500 * (general_ouro_branco - general_ouro_preto) + 500 * (general_prata_branco- general_prata_preto) + 300 * (cavalo_branco - cavalo_preto) + 300 * (lanca_branca - lanca_preta)

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
    

# ALPHABETA
# Auxilia em diminuir os calculos de profundidade, ao invés de calcular a arvore interira ele vai até o que ja é melhor
# É a utilizada para o calculo das possibilidade, nível a nível
# Se chegou no fim da profundidade parametrizada, apenas calcula quisce
# se não chegou no final, apronfunda e calcula
# Se em um dos movimentos simulados alcançou uma pontuação maior que beta (que já é o do adversario), finaliza o calculo e retorna esse movimento que ganha
# Se é maior que o alpha ja armazenado, guarda e segue os procimos calculos

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

# QUIESCE
# Pontuação do tabuleiro
# se for maior que o beta retorna beta (finaliza)
# Maior que o alpha, armazena na pontuação do tabuleiro
# Além disso vai calcular se a posição final tem uma captura de peça, se houver ele deverá fazer a simulaçã desse movimento e não deve finalizar os calculos antes disso

# Ao fim retorna Alpha
def is_capture(board, move):
    # Obtém a peça na posição de destino do movimento
    piece_at_destination = board.piece_at(move.to_square)

    # Verifica se há uma peça na posição de destino e se ela pertence ao adversário
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

# '''SelectMove (vai escolher o movimento baseado nas possibilidades de alphabeta)
# depth é a profundidade
# Não fará nada a principio e checará os movimentos possíveis
# Ele ira simular as jogadas e calcular o valor encontrado, cada vez que ele encontrar um movimento com valor superior ao movimento anterior, ele irá armazenar
# bestValue > bestMove > move
# Se o valor for melhor que o alpha (que é o valor inicial da jogada) armazena em alpha por enquanto
# No fim com um pop ele desfaz o movimento e recalcula o proximo (sempre armazenando os melhores vaore/movimentos)'''

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



while not board.is_game_over():
    if board.turn:
        move = selectmove(3)
        board.push(move)
        print(board)
    else:
        move = selectmove(3)
        board.push(move)
        print(board)
        

board

board.reset_board()