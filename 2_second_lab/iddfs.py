
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': [],
    'G': ['J'],
    'H': [],
    'I': [],
    'J': []
}

# Depth Limited Search
def dls(node, goal, depth):

    print(node, end=" ")

    if node == goal:
        return True

    if depth <= 0:
        return False

    for child in graph[node]:
        if dls(child, goal, depth - 1):
            return True

    return False


# Iterative Deepening DFS
def iddfs(start, goal, max_depth):

    for depth in range(max_depth + 1):

        print("\nDepth:", depth)
        print("Traversal:", end=" ")

        if dls(start, goal, depth):
            print("\nGoal Found!")
            return True

    print("\nGoal Not Found!")
    return False


start = 'A'
goal = 'G'

iddfs(start, goal, 5)
