import math


# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(row)
    print()


# Check if the board is in a terminal state and return the utility value
def evaluate(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] != '_':
            return 1 if row[0] == 'X' else -1

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '_':
            return 1 if board[0][col] == 'X' else -1

    if board[0][0] == board[1][1] == board[2][2] != '_':
        return 1 if board[0][0] == 'X' else -1

    if board[0][2] == board[1][1] == board[2][0] != '_':
        return 1 if board[0][2] == 'X' else -1

    # Return 0 if it's a tie (no winner and no empty spaces left)
    if all(cell != '_' for row in board for cell in row):
        return 0

    return None  # Game is still ongoing


# Check if there are any moves left
def is_moves_left(board):
    for row in board:
        if '_' in row:
            return True
    return False


# Minimax function to return the best possible move
def minimax(board, is_maximizing):
    score = evaluate(board)

    # If the game has ended, return the utility value
    if score is not None:
        return score

    if is_maximizing:  # O's turn (MAX player)
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':  # Check for an empty cell
                    board[i][j] = 'O'  # Make a move
                    best_score = max(best_score, minimax(board, False))  # Recursive minimax call
                    board[i][j] = '_'  # Undo the move
        return best_score
    else:  # X's turn (MIN player)
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':  # Check for an empty cell
                    board[i][j] = 'X'  # Make a move
                    best_score = min(best_score, minimax(board, True))  # Recursive minimax call
                    board[i][j] = '_'  # Undo the move
        return best_score


# Function to find the best move for O (MAX player)
def find_best_move(board):
    best_move = None
    best_value = -math.inf

    # Check all possible moves
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':  # If the cell is empty
                board[i][j] = 'O'  # Try O's move
                move_value = minimax(board, False)  # Call minimax for X's turn (MIN player)
                board[i][j] = '_'  # Undo the move

                # Update best move if a better move is found
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)

    return best_move, best_value


# Example Tic-Tac-Toe board state
board = [
    ['X', 'O', 'X'],
    ['X', '_', 'O'],
    ['_', '_', '_']
]

# Print the current board
print("Current board state:")
print_board(board)

# Find the best move for O (MAX player)
best_move, best_value = find_best_move(board)

# Print the result
if best_move:
    print(f"Best move for O is at position {best_move} with a minimax value of {best_value}.")
else:
    print("No valid moves left.")

# Show the terminal nodes utility value
print("Terminal Nodes and their utility values:")
for i in range(3):
    for j in range(3):
        if board[i][j] == '_':
            board[i][j] = 'O'
            score = minimax(board, False)
            board[i][j] = '_'
            print(f"Move O to position ({i}, {j}) results in a utility value of {score}.")
