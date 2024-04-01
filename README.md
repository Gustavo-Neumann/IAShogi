# IAShogi
Necessario instalar a biblioteca python-shogi:

pip install python-shogi

Usar a funcao move_piece(board) para jogar contra a ia

while not board.is_game_over():
    if board.turn:
        # Funcao para jogar contra a IA
        # move_piece(board) <<<<<<

        # Funcao que joga movimentos aleatorios
        board.push(random_move(board))
        print(board)
    else:
        # IA Jogando
        move = selectmove(3)
        board.push(move)
        print(board)
        
