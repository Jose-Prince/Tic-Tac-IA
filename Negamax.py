import random

EMPTY = None
PLAYER_X = 'X'  # IA (Max)
PLAYER_O = 'O'  # Rival (random)

def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] is not None:
            return board[a]
    return None

def is_terminal(state):
    return check_winner(state) is not None or all(cell is not None for cell in state)

def evaluate(state):
    winner = check_winner(state)
    if winner == PLAYER_X:
        return 1
    elif winner == PLAYER_O:
        return -1
    else:
        return 0

def applyAction(state, action, player):
    newState = state[:]
    newState[action] = player
    return newState

def getAvailableActions(state):
    return [i for i in range(9) if state[i] is None]

def generate_moves(state, player):
    return [
        (i, applyAction(state, i, player))
        for i in getAvailableActions(state)
    ]

def negamax(state, depth, alpha, beta, color):
    if depth == 0 or is_terminal(state):
        return color * evaluate(state)

    max_eval = float('-inf')
    player = PLAYER_X if color == 1 else PLAYER_O

    for _, child in generate_moves(state, player):
        eval = -negamax(child, depth - 1, -beta, -alpha, -color)
        if eval > max_eval:
            max_eval = eval
        if max_eval > alpha:
            alpha = max_eval
        if alpha >= beta:
            break
    return max_eval

def best_move_negamax(state, depth):
    best_val = float('-inf')
    best_action = None
    for action, child in generate_moves(state, PLAYER_X):
        val = -negamax(child, depth - 1, float('-inf'), float('inf'), -1)
        if val > best_val:
            best_val = val
            best_action = action
    return best_action

def gameSimulation_negamax(first='X', N=1000, k=9):
    victories = 0
    defeats = 0
    draws = 0

    for _ in range(N):
        state = [None] * 9
        currentPlayer = first

        while not is_terminal(state):
            if currentPlayer == PLAYER_X:
                move = best_move_negamax(state, k)
            else:
                # Jugador O es random
                moves = getAvailableActions(state)
                move = random.choice(moves)

            state = applyAction(state, move, currentPlayer)
            currentPlayer = PLAYER_O if currentPlayer == PLAYER_X else PLAYER_X

        winner = check_winner(state)
        if winner == PLAYER_X:
            victories += 1
        elif winner == PLAYER_O:
            defeats += 1
        else:
            draws += 1

    return victories, defeats, draws


if __name__ == "__main__":
    print("Negamax juega X (empieza X):", gameSimulation_negamax(first='X', N=1000, depth=9))
    print("Negamax juega X (empieza O):", gameSimulation_negamax(first='O', N=1000, depth=9))

