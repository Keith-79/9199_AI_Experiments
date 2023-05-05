from queue import PriorityQueue

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def __lt__(self, other):
        return False

    def __eq__(self, other):
        return (self.missionaries == other.missionaries and
                self.cannibals == other.cannibals and
                self.boat == other.boat)

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0:
            return False
        if self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.cannibals > self.missionaries and self.missionaries > 0:
            return False
        if 3 - self.cannibals > 3 - self.missionaries and 3 - self.missionaries > 0:
            return False
        return True

    def get_successors(self):
        successors = []
        if self.boat == 'left':
            for i in range(3):
                for j in range(3):
                    state = State(self.missionaries - i, self.cannibals - j, 'right')
                    if state.is_valid():
                        successors.append((state, i+j))
        else:
            for i in range(3):
                for j in range(3):
                    state = State(self.missionaries + i, self.cannibals + j, 'left')
                    if state.is_valid():
                        successors.append((state, i+j))
        return successors

    def heuristic(self):
        return self.missionaries + self.cannibals

def gbfs(start_state):
    visited = set()
    pq = PriorityQueue()
    pq.put((start_state.heuristic(), start_state, []))

    while not pq.empty():
        _, state, path = pq.get()

        if state not in visited:
            visited.add(state)

            if state.missionaries == 0 and state.cannibals == 0 and state.boat == 'right':
                return path + [(state, 0)]

            for successor, _ in state.get_successors():
                pq.put((successor.heuristic(), successor, path + [(state, 1)]))

    return None

start_state = State(3, 3, 'left')
solution = gbfs(start_state)

if solution is None:
    print("No solution found")
else:
    print("Solution found with cost", solution[-1][1])
    for state, step_cost in solution:
        print(f"{state.missionaries}M {state.cannibals}C {state.boat}")
