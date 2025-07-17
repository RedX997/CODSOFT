import random

human = "X"
ai = "O"

def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(" | ".join([board[i + j] if board[i + j] else str(i + j + 1) for j in range(3)]))
        if i < 6:
            print("---------")
    print()

def check_winner(board):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in wins:
        a, b, c = combo
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if all(board):
        return "Draw"
    return None

def minimax(board, depth, is_max):
    winner = check_winner(board)
    if winner:
        scores = {human: -1, ai: 1, "Draw": 0}
        return scores[winner]

    if is_max:
        best = float('-inf')
        for i in range(9):
            if not board[i]:
                board[i] = ai
                best = max(best, minimax(board, depth + 1, False))
                board[i] = ""
        return best
    else:
        best = float('inf')
        for i in range(9):
            if not board[i]:
                board[i] = human
                best = min(best, minimax(board, depth + 1, True))
                board[i] = ""
        return best

def best_move(board):
    best_score = float('-inf')
    move = None
    for i in range(9):
        if not board[i]:
            board[i] = ai
            score = minimax(board, 0, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move

def main():
    board = [""] * 9
    print("🎮 Tic-Tac-Toe AI Game")
    print_board(board)

    while True:
        try:
            move = int(input("Your move (1-9): ")) - 1
            if board[move] == "":
                board[move] = human
            else:
                print("Cell already filled!")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Choose a number between 1 and 9.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🏆 {winner} wins!" if winner != "Draw" else "It's a Draw!")
            break

        ai_move = best_move(board)
        if ai_move is not None:
            board[ai_move] = ai
            print("\nAI played its move...")
        
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"🏆 {winner} wins!" if winner != "Draw" else "It's a Draw!")
            break

if __name__ == "__main__":
    main()
