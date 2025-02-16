def printboard(board):
    """Function to print the Tic-Tac-Toe board"""
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
    print("-----|-----|-----")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
    print("-----|-----|-----")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")

def check_winner(board, player):
    """Function to check if a player has won"""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

if __name__ == "__main__":
    board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']  # Initial board
    current_player = 'X'  # X always starts

    for turn in range(9):  # Max 9 moves
        printboard(board)
        while True:
            try:
                move = int(input(f"Player {current_player}, enter your move (0-8): "))
                if 0 <= move <= 8 and board[move] not in ['X', 'O']:
                    board[move] = current_player
                    break
                else:
                    print("❌ Invalid move! Choose an empty spot between 0-8.")
            except ValueError:
                print("❌ Invalid input! Enter a number between 0-8.")

        # Check for a winner
        if check_winner(board, current_player):
            printboard(board)
            print(f"🏆 Player {current_player} wins! 🏆")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

    else:
        printboard(board)
        print("🤝 It's a Draw! 🤝")
