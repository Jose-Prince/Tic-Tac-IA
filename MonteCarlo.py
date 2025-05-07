import random
import math
import time

class Node:
    def __init__(self, state, parent=None):
        self.state = state
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
    newState = applyAction(node.state, action)
    child = Node(newState, parent=node)
    node.children.append(child)
    return child

def rollout(node):
    currentState = node.state
    while not isTerminal(currentState):
        actions = getAvailableActions(currentState)
        if not actions:
            break
        action = random.choice(actions)
        currentState = applyAction(currentState, action)
    return getResult(currentState)

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
    pass

def applyAction(state, action):
    pass

def isTerminal(state):
    pass

def getResult(state):
    pass
