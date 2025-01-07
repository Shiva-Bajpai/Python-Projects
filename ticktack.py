def print_board(board):
    print("\n".join([" | ".join(row) for row in board]))
    
def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter column (0-2): "))
        
        if board[row][col] != " ":
            print("Cell already taken! Try again.")
            continue
        board[row][col] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if all(board[row][col] != " " for row in range(3) for col in range(3)):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
