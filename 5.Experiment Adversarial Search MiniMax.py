import sys

# Constants
X = "X"
O = "O"
EMPTY = " "
BOARD_SIZE = 3

# Utility function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * (BOARD_SIZE * 2 - 1))

# Utility function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for i in range(BOARD_SIZE):
        if all(board[j][i] == player for j in range(BOARD_SIZE)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)) or all(
        board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)
    ):
        return True

    return False

# Utility function to check if the game is a draw
def check_draw(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

# Minimax algorithm
def minimax(board, depth, maximizing_player):
    # Base case: check if the game is over
    if check_winner(board, X):
        return 1
    elif check_winner(board, O):
        return -1
    elif check_draw(board):
        return 0

    if maximizing_player:
        max_eval = -sys.maxsize
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == EMPTY:
                    board[i][j] = X
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = sys.maxsize
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == EMPTY:
                    board[i][j] = O
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

# Main function to play Tic Tac Toe
def play_tic_tac_toe():
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    current_player = X

    while True:
        if current_player == X:
            row = int(input("Enter row (0-2) for {}: ".format(current_player)))
            col = int(input("Enter col (0-2) for {}: ".format(current_player)))
            if board[row][col] != EMPTY:
                print("Invalid move. Try again.")
                continue
        else:
            print("Computer's turn...")
            best_eval = -sys.maxsize
            best_move = None
            for i in range(BOARD_SIZE):
                for j in range(BOARD_SIZE):
                    if board[i][j] == EMPTY:
                        board[i][j] = O
                        eval = minimax(board, 0, True)
                        board[i][j] = EMPTY
                        if eval > best_eval:
                            best_eval = eval
                            best_move = (i, j)
            row, col = best_move

        board[row][col] = current_player
        # Print the updated board
        print_board(board)

        # Check if the current player wins
        if check_winner(board, current_player):
            print("{} wins!".format(current_player))
            break

        # Check if the game is a draw
        if check_draw(board):
            print("It's a draw!")
            break

        # Switch to the next player
        current_player = O if current_player == X else X

if __name__ == "__main__":
    play_tic_tac_toe()
