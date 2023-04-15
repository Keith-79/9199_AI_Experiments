import numpy as np
import random

def magic_square(n):
    # create magic square of size n
    magic = np.zeros((n,n), dtype=int)
    i, j = 0, n//2
    for num in range(1, n*n+1):
        magic[i, j] = num
        if num % n == 0:
            i, j = (i+1) % n, j
        else:
            i, j = (i-1+n) % n, (j+1) % n
    return magic

def print_board(board):
    # print current state of the board
    n = board.shape[0]
    for i in range(n):
        row = '|'.join([str(board[i,j]) if board[i,j] != 0 else ' ' for j in range(n)])
        print(row)
        if i != n-1:
            print('-'*(n*2-1))

def get_move(player, board):
    # get move from player or AI and update the board
    valid_move = False
    while not valid_move:
        if player == 1:
            move = input(f"Player {player}, please choose a position (1-{board.shape[0]**2}): ")
            try:
                move = int(move) - 1
                i, j = move // board.shape[0], move % board.shape[0]
                if board[i,j] == 0:
                    board[i,j] = player
                    valid_move = True
                else:
                    print("Invalid move. That position is already taken.")
            except:
                print("Invalid input. Please enter a number between 1 and ", board.shape[0]**2)
        else:
            i, j = random.randint(0, board.shape[0]-1), random.randint(0, board.shape[0]-1)
            if board[i,j] == 0:
                board[i,j] = player
                valid_move = True
        if valid_move:
            return

def check_win(board):
    # check if there is a winner
    n = board.shape[0]
    magic = magic_square(n)
    for i in range(n):
        if np.array_equal(board[i,:], [1]*n) or np.array_equal(board[i,:], [2]*n):
            return True
        if np.array_equal(board[:,i], [1]*n) or np.array_equal(board[:,i], [2]*n):
            return True
    if np.array_equal(board.diagonal(), [1]*n) or np.array_equal(board.diagonal(), [2]*n):
        return True
    if np.array_equal(np.fliplr(board).diagonal(), [1]*n) or np.array_equal(np.fliplr(board).diagonal(), [2]*n):
        return True
    if np.sum(board*magic[board-1]) == 15:
        return True
    return False

def play_game():
    # main function to play the game
    n = 3
    board = np.zeros((n,n), dtype=int)
    players = [1, 2]
    current_player = players[0]
    print_board(board)
    while not check_win(board):
        get_move(current_player, board)
        print_board(board)
        if current_player == players[0]:
            current_player = players[1]
        else:
            current_player = players[0]
    if current_player == players[0]:
            current_player = players[1]
    else:
        current_player = players[0]
    print(f"Player {current_player} wins!")

play_game()
