def find_zeros(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbours(state):
    neighbours = []
    r, c = find_zeros(state)
    directions = {"Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1)}
    for move, (dr, dc) in directions.items():
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = [row[:] for row in state]
            new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
            neighbours.append((new_state, move))
    return neighbours


def dfs(start, goal, max_depth=10):
    stack = [(start, [], 0)]
    visited = set()

    while stack:
        state, path, depth = stack.pop()
        hash_state = tuple(tuple(row) for row in state)

        if hash_state in visited:
            continue
        visited.add(hash_state)
        if state == goal:
            return path
        if depth > max_depth:
            continue

        for neighbour, move in get_neighbours(state):
            stack.append((neighbour, path + [move], depth + 1))
    return None


def get_input():
    state = []
    for i in range(3):
        row = list(map(int, input().split()))
        state.append(row)
    return state


print("8 Puzzle using DFS")
print("Enter the start state: ")
start = get_input()
print("Enter the goal state: ")
goal = get_input()

solution = dfs(start, goal)

if solution:
    curr = [row[:] for row in start]
    for move in solution:
        for neigh, m in get_neighbours(curr):
            if m == move:
                curr = neigh
                print(m)
                for i in curr:
                    print(i)
                print()
                break
else:
    print("No Solution")
