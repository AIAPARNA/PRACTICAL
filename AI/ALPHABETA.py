import math

board = [" "] * 9
HUMAN, AI = "X", "O"

def print_board():
    for r in [board[i:i+3] for i in range(0, 9, 3)]:
        print("| " + " | ".join(r) + " |")

def win(b, p):
    w = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    # ✅ fixed variable shadowing
    return any(b[i] == b[j] == b[k] == p for i, j, k in w)

def minimax(b, depth, alpha, beta, isMax):
    if win(b, AI): return 10 - depth
    if win(b, HUMAN): return depth - 10
    if " " not in b: return 0  # draw

    if isMax:  # AI turn
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = AI
                val = minimax(b, depth + 1, alpha, beta, False)
                b[i] = " "
                best = max(best, val)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break  # prune
        return best

    else:  # Human turn
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = HUMAN
                val = minimax(b, depth + 1, alpha, beta, True)
                b[i] = " "
                best = min(best, val)
                beta = min(beta, best)
                if beta <= alpha:
                    break  # prune
        return best

def best_move():
    bestVal, move = -math.inf, None
    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            val = minimax(board, 0, -math.inf, math.inf, False)
            board[i] = " "
            if val > bestVal:
                bestVal, move = val, i
    return move

print("You = X  |  AI = O")
print_board()

while True:
    pos = int(input("Enter (1-9): ")) - 1

    if board[pos] != " ":
        print("Invalid!")
        continue

    board[pos] = HUMAN
    print_board()

    if win(board, HUMAN):
        print("You win!")
        break

    if " " not in board:
        print("Draw!")
        break

    ai = best_move()
    board[ai] = AI
    print("\nAI move:")
    print_board()

    if win(board, AI):
        print("AI wins!")
        break

    if " " not in board:
        print("Draw!")
        break