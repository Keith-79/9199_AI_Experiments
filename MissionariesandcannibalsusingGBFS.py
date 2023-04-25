from queue import PriorityQueue

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.heuristic = heuristic
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1
    
    def __lt__(self, other):
        return (self.path_cost + self.heuristic) < (other.path_cost + other.heuristic)

def gbfs(start_state, goal_state, heuristic):
    start_node = Node(start_state, None, None, 0, heuristic(start_state))
    frontier = PriorityQueue()
    frontier.put(start_node)
    explored = set()
    
    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.state
        
        if current_state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]
        
        explored.add(current_state)
        
        for next_state, action, cost in get_successors(current_state):
            if next_state not in explored:
                next_node = Node(next_state, current_node, action, current_node.path_cost + cost, heuristic(next_state))
                frontier.put(next_node)
    
    return None

def get_successors(state):
    m, c, b = state
    successors = []
    
    if b == 1:
        for mm in range(3):
            for cc in range(3):
                if mm + cc == 0 or mm + cc > 2:
                    continue
                next_state = (m - mm, c - cc, 0)
                if next_state[0] >= 0 and next_state[1] >= 0 and next_state[0] <= 3 and next_state[1] <= 3 and (next_state[0] == 0 or next_state[0] >= next_state[1]):
                    successors.append((next_state, (mm, cc, 0), 1))
    else:
        for mm in range(3):
            for cc in range(3):
                if mm + cc == 0 or mm + cc > 2:
                    continue
                next_state = (m + mm, c + cc, 1)
                if next_state[0] >= 0 and next_state[1] >= 0 and next_state[0] <= 3 and next_state[1] <= 3 and (next_state[0] == 3 or next_state[0] >= next_state[1]):
                    successors.append((next_state, (mm, cc, 1), 1))
    
    return successors

def h(state):
    return abs(state[0] - 3) + abs(state[1] - 3)

path = gbfs((3,3,1), (0,0,0), h)
[print(i) for i in path]