import random
import math
import time

class Node:
    def __init__(self, state, player, parent=None):
        self.state = state
        self.player = player
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0
        self.untriedActions = getAvailableActions(state)

def monteCarloTreeSearch(root, timeLimit=1.0):
    endTime = time.time() + timeLimit

    while time.time() < endTime:
        leaf = traverse(root)
        simulationResult = rollout(leaf)
        backpropagate(leaf, simulationResult)

    return bestChild(root)

def traverse(node):
    while fullyExpanded(node) and node.children:
        node = bestUct(node)
    if node.untriedActions:
        return expand(node)
    return node

def expand(node):
    action = node.untriedActions.pop()
    newState = applyAction(node.state, action, node.player)
    nextPlayer = 'O' if node.player == 'X' else 'X'
    child = Node(newState, nextPlayer, parent=node)
    node.children.append(child)
    return child

def rollout(node):
    currentState = node.state
    currentPlayer = node.player
    while not isTerminal(currentState):
        actions = getAvailableActions(currentState)
        if not actions:
            break
        action = random.choice(actions)
        currentState = applyAction(currentState, action, currentPlayer)
        currentPlayer = 'O' if currentPlayer == 'X' else 'X'
    return getResult(currentState, node.player)

def backpropagate(node, result):
    while node is not None:
        node.visits += 1
        node.value += result
        node = node.parent

def bestUct(node):
    logN = math.log(node.visits)
    return max(node.children, key=lambda child: uctScore(child, logN))

def uctScore(child, logN):
    if child.visits == 0:
        return float('inf')
    exploitation = child.value / child.visits
    exploration = math.sqrt(logN / child.visits)
    c = math.sqrt(2)
    return exploitation + c * exploration

def bestChild(node):
    return max(node.children, key=lambda child: child.visits)

def fullyExpanded(node):
    return len(node.untriedActions) == 0

def getAvailableActions(state):
    return [i for i in range(9) if state[i] is None]

def applyAction(state, action, player):
    newState = state[:]
    newState[action] = player
    return newState

def isTerminal(state):
    return checkWinner(state) is not None or all(cell is not None for cell in state)

def getResult(state, player):
    winner = checkWinner(state)
    if winner == player:
        return 1 # Win
    elif winner is None:
        return 0 # Draw
    else:
        return -1 # Loose

def checkWinner(state):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)] # Different ways a game is won
    for i, j, k in wins:
        if state[i] and state[i] == state[j] == state[k]:
            return state[i]
    return None

def printBoard(state):
    chars = [c if c else ' ' for c in state]
    for i in range(0, 9, 3):
        print(f"{chars[i]} | {chars[i+1]} | {chars[i+2]}")
        if i < 6:
            print("--+---+--")

def gameSimulation(N=1000, t=1.0):
    timeWinX=0
    timeWinO=0
    timeDraw=0
    for _ in range(N):
        state = [None] * 9
        startPlayer = random.choice(['X','O'])
        currentPlayer = startPlayer
        turn = 1

        while not isTerminal(state):
            if currentPlayer == 'X':
                move = random.choice(getAvailableActions(state))
            else:
                root = Node(state, currentPlayer)
                bestNode = monteCarloTreeSearch(root, timeLimit=t)
                move = [i for i in range(9) if state[i] != bestNode.state[i]][0]

            state = applyAction(state, move, currentPlayer)
            currentPlayer = 'O' if currentPlayer == 'X' else 'X'
            turn += 1

        winner = checkWinner(state)
        if winner:
            if currentPlayer == 'X':
                timeWinO += 1
            else:
                timeWinX += 1
        else:
            timeDraw += 1

gameSimulation(t=0.2)
