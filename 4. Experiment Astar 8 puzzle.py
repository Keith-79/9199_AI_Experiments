import heapq

# Define the goal state
goal_state = [[1,2,3],[4,5,6],[7,8,0]]

# Define the heuristic function (Manhattan distance)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                distance += abs(i - (state[i][j]-1)//3) + abs(j - (state[i][j]-1)%3)
    return distance

# Define the A* algorithm
def solve(initial_state):
    frontier = []
    visited = set()
    heapq.heappush(frontier, (heuristic(initial_state), initial_state, 0, None))
    while frontier:
        _, current_state, g, parent = heapq.heappop(frontier)
        if current_state == goal_state:
            moves = []
            while parent is not None:
                moves.append(current_state)
                current_state, parent = parent
            moves.append(current_state)
            return moves[::-1]
        visited.add(tuple(map(tuple, current_state)))
        for r, row in enumerate(current_state):
            for c, val in enumerate(row):
                if val == 0:
                    break
            if val == 0:
                break
        for dr, dc in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            if 0 <= r+dr < 3 and 0 <= c+dc < 3:
                new_state = [row[:] for row in current_state]
                new_state[r][c], new_state[r+dr][c+dc] = new_state[r+dr][c+dc], new_state[r][c]
                if tuple(map(tuple, new_state)) not in visited:
                    heapq.heappush(frontier, (heuristic(new_state)+g+1, new_state, g+1, (current_state, parent)))
    return None

# Example usage
initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
solution = solve(initial_state)
if solution is not None:
    for state in solution:
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
