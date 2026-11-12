
import heapq

# Initial and goal states
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Manhattan Distance Heuristic
def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            x = i // 3
            y = i % 3

            goal_pos = state[i] - 1
            gx = goal_pos // 3
            gy = goal_pos % 3

            distance += abs(x - gx) + abs(y - gy)

    return distance


# Display puzzle
def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# A* Algorithm
def solve(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, []))

    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)

        path = path + [state]

        if state == goal:
            print("Solution Found!")
            for s in path:
                display(s)
            print("Total Moves:", len(path) - 1)
            return

        zero = state.index(0)

        moves = [-3, 3, -1, 1]

        for move in moves:
            new_pos = zero + move

            if 0 <= new_pos < 9:
                if move == -1 and zero % 3 == 0:
                    continue
                if move == 1 and zero % 3 == 2:
                    continue

                new_state = list(state)

                new_state[zero], new_state[new_pos] = (
                    new_state[new_pos], new_state[zero]
                )

                new_state = tuple(new_state)

                if new_state not in visited:
                    new_g = g + 1
                    new_f = new_g + heuristic(new_state)

                    heapq.heappush(
                        pq, (new_f, new_g, new_state, path)
                    )

    print("No solution found!")


solve(start)
