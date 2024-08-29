def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                return move
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def update_board(board, move, player):
    row = (move - 1) // 3
    col = (move - 1) % 3

    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        print("Invalid move. The cell is already occupied. Please try again.")
        return False

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    print("Let's play Tic Tac Toe!")

    while True:
        print_board(board)

        move = get_player_move()

        if update_board(board, move, current_player):
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_tic_tac_toe()
