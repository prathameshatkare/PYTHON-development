# Tic-Tac-Toe Game in Python

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if any player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([spot == player for spot in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

# Function to check if the board is full (draw)
def check_draw(board):
    return all([spot != " " for row in board for spot in row])

# Main function to play the game
def play_game():
    # Initialize empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        row = int(input(f"Player {players[current_player]}, enter row (1-3): ")) - 1
        col = int(input(f"Player {players[current_player]}, enter column (1-3): ")) - 1

        # Check if the selected cell is empty
        if board[row][col] == " ":
            board[row][col] = players[current_player]

            # Check if current player has won
            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                break

            # Check if the game is a draw
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch player
            current_player = 1 - current_player
        else:
            print("Cell already taken! Try again.")

if __name__ == "__main__":
    play_game()
