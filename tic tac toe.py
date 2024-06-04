import random
from typing import List, Tuple, Optional

# Print the board
def print_board(board: List[List[str]]) -> None:
    print("\n")
    print("    1   2   3 ")
    print("  -------------")
    for idx, row in enumerate(board):
        print(f"{idx + 1} | " + " | ".join(row) + " |")
        print("  -------------")
    print("\n")

# Check for a winner
def check_winner(board: List[List[str]]) -> Optional[str]:
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

# Check for a draw
def is_draw(board: List[List[str]]) -> bool:
    for row in board:
        if ' ' in row:
            return False
    return True

# Get valid moves
def valid_moves(board: List[List[str]]) -> List[Tuple[int, int]]:
    moves = []
    for row in range(3):
        for column in range(3):
            if board[row][column] == " ":
                moves.append((row, column))
    return moves

# Computer makes a move
def comp_move(board: List[List[str]]) -> None:
    moves = valid_moves(board)
    move = random.choice(moves)
    board[move[0]][move[1]] = "O"

# Main game loop
def main() -> None:
    print("        ∆∆∆    Welcome to the Tic Tac Toe Game:    ∆∆∆\n")
    choice = int(input("1. One Player (Vs Computer)\n2. Two Players\nEnter your choice: "))
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        if current_player == 'X':
            while True:
                try:
                    print("~~~ ∆∆∆ Player 1 Turn ∆∆∆ ~~~")
                    row, column = map(int, input("Enter Row and Column (1,2,3): ").split())
                    row -= 1
                    column -= 1
                    if row < 3 and column < 3 and board[row][column] == " ":
                        board[row][column] = current_player
                        break
                    else:
                        print("The move is already taken. Enter valid coordinates.")
                except:
                    print("Invalid input! Please enter numbers between 1 and 3.")
        else:
            if choice == 1:
                print("~~~ ∆∆∆ Computer Turn ∆∆∆ ~~~")
                comp_move(board)
            else:
                while True:
                    try:
                        print("~~~ ∆∆∆ Player 2 Turn ∆∆∆ ~~~")
                        row, column = map(int, input("Enter Row and Column (1,2,3): ").split())
                        row -= 1
                        column -= 1
                        if row < 3 and column < 3 and board[row][column] == " ":
                            board[row][column] = current_player
                            break
                        else:
                            print("The move is already taken. Enter valid coordinates.")
                    except:
                        print("Invalid input! Please enter numbers between 1 and 3.")

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print(f"{'∆∆∆ Player 1 Wins! ∆∆∆' if winner == 'X' else '∆∆∆ Player 2 Wins! ∆∆∆' if choice == 2 else '∆∆∆ Computer Wins! ∆∆∆'}")
            print_board(board)
            break

        # Check for a draw
        if is_draw(board):
            print("~~~ ∆∆∆ Game Draw! ∆∆∆ ~~~")
            print_board(board)
            break

        # Toggle player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    main()