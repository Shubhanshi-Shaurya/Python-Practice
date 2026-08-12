board = [" " for _ in range(9)]
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()
def check_winner(player):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False
def is_full():
    return " " not in board
def minimax(is_maximizing):
    if check_winner("X"):
        return 1
    if check_winner("O"):
        return -1
    if is_full():
        return 0
    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score
def ai_move():
    best_score = -float("inf")
    best_move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "X"
print("TIC TAC TOE")
print("Computer = X, Player = O")
print("Enter positions from 0 to 8")
while True:
    ai_move()
    print_board()
    if check_winner("X"):
        print("Computer wins!")
        break
    if is_full():
        print("It's a draw!")
        break
    while True:
        move = int(input("Enter your move (0-8): "))
        if 0 <= move <= 8 and board[move] == " ":
            board[move] = "O"
            break
        print("Invalid move!")
    if check_winner("O"):
        print_board()
        print("You win!")
        break
    if is_full():
        print_board()
        print("It's a draw!")
        break