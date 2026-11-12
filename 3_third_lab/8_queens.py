import random

def calculate_heuristic(state):
    """Calculates the number of attacking queen pairs."""
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            # Same row
            if state[i] == state[j]:
                attacks += 1
            # Same diagonal
            elif abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_best_neighbor(state):
    """Finds the best neighboring states by moving one queen in its column."""
    current_h = calculate_heuristic(state)
    best_h = current_h
    best_neighbors = []
    n = len(state)

    for col in range(n):
        original_row = state[col]
        for row in range(n):
            if row == original_row:
                continue

            # Create a neighbor state
            neighbor = list(state)
            neighbor[col] = row
            neighbor_h = calculate_heuristic(neighbor)

            if neighbor_h < best_h:
                best_h = neighbor_h
                best_neighbors = [neighbor]
            elif neighbor_h == best_h:
                best_neighbors.append(neighbor)

    if best_h < current_h and best_neighbors:
        # Return one of the best states randomly
        return random.choice(best_neighbors), best_h

    return None, current_h

def hill_climbing(max_restarts=100):
    """Solves the 8 Queens problem using Hill Climbing with random restarts."""
    n = 8
    for attempt in range(1, max_restarts + 1):
        # Initialize random state
        state = [random.randint(0, n - 1) for _ in range(n)]
        current_h = calculate_heuristic(state)

        while True:
            neighbor, neighbor_h = get_best_neighbor(state)
            if neighbor is None:  # Local minimum reached
                break
            state = neighbor
            current_h = neighbor_h

        if current_h == 0:
            print(f"Solved successfully on attempt {attempt}!")
            return state

    print("Failed to find a solution within max restarts.")
    return state

def print_board(state):
    """Helper function to visualize the board configuration."""
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)

# Run the algorithm
solution = hill_climbing()
print(f"\nFinal State Array representation (columns 0-7): {solution}")
print(f"Remaining attacking pairs: {calculate_heuristic(solution)}\n")
print_board(solution)