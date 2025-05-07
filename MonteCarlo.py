def monteCarloTreeSearch(root):
    while resourcesLeft(time, computational power):
        leaf = traverse(root)
        simulationResult = rollout(leaf)
        backpropagate(leaf, simulationResult)

    return bestChild(root)

def traverse(node):
    while fullyExpanded(node):
        node = bestUct(node)

    return pickUnvisited(node.children) or node

def rollout(node):
    while nonTerminal(node):
        node = rolloutPolicy(node)
    return result(node)

def rolloutPolicy(node):
    return pickRandom(node.children)

def backpropagate(node, result):
    if isRoot(node) return
    node.stats = updateStats(node, result)
    backpropagate(node.parent)

def bestChildren(node):
    #pick child with highest number of visits
