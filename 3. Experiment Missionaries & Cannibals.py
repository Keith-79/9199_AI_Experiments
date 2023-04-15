from typing import Tuple, List

# Define the game state as a tuple of three integers (M, C, B), where:
# - M is the number of missionaries on the left bank.
# - C is the number of cannibals on the left bank.
# - B is the location of the boat: 1 for the left bank, 0 for the right bank.
# Initially, there are 3 missionaries, 3 cannibals, and the boat is on the left bank.
INITIAL_STATE = (3, 3, 1)

# Define the goal state, which is the opposite of the initial state: all missionaries,
# cannibals, and the boat on the right bank.
GOAL_STATE = (0, 0, 0)

# Define the legal moves as a list of tuples, where each tuple contains the number of
# missionaries and cannibals that are moved in the boat. The moves are legal if they
# do not leave either side of the river with more cannibals than missionaries.
LEGAL_MOVES = [(1, 0), (2, 0), (1, 1), (0, 1), (0, 2)]


def is_legal(state: Tuple[int, int, int]) -> bool:
    """Check if a given state is legal, i.e., does not leave either side of the river with
    more cannibals than missionaries."""
    m, c, b = state
    if m < c and m > 0:  # more cannibals than missionaries on left bank
        return False
    if 3-m < 3-c and 3-m > 0:  # more cannibals than missionaries on right bank
        return False
    return True



def apply_move(state: Tuple[int, int, int], move: Tuple[int, int]) -> Tuple[int, int, int]:
    """Apply a legal move to a state and return the resulting state."""
    m, c, b = state
    dm, dc = move
    if b == 1:  # boat is on the left bank
        return (m-dm, c-dc, 0)
    else:  # boat is on the right bank
        return (m+dm, c+dc, 1)


def is_goal(state: Tuple[int, int, int]) -> bool:
    """Check if a given state is the goal state."""
    return state == GOAL_STATE


def get_legal_moves(state: Tuple[int, int, int]) -> List[Tuple[int, int]]:
    """Return a list of legal moves that can be applied to a state."""
    m, c, b = state
    moves = []
    for dm in range(3):
        for dc in range(3):
            if dm + dc > 0 and dm + dc <= 2:
                move = (dm, dc)
                new_state = apply_move(state, move)
                if is_legal(new_state):
                    moves.append(move)
    return moves

def print_state(state: Tuple[int, int, int]) -> None:
    """Print a human-readable representation of a state."""
    m, c, b = state
    print(f"{m}M {c}C {'B' if b == 1 else ' '} {' ' if b == 1 else 'B'} {3-m}M {3-c}C")


def solve(initial_state: Tuple[int, int, int]) -> None:
    # Initialize the frontier with the initial state.
    frontier = [initial_state]
    # Initialize the explored set as an empty set.
    explored = set()
    # Initialize the path dictionary as an empty dictionary.
    path = {}
    # Add the initial state to the path dictionary with a None parent.
    path[initial_state] = None
    # Keep looping until the frontier is empty.
    while frontier:
        # Get the next state from the frontier.
        state = frontier.pop(0)
        # If the state is the goal state, print the solution and return.
        if is_goal(state):
            print_solution(path, state)
            return
        # Add the state to the explored set.
        explored.add(state)
        # Get the legal moves for the state.
        moves = get_legal_moves(state)
        # Loop over the legal moves.
        for move in moves:
            # Apply the move to the state to get the new state.
            new_state = apply_move(state, move)
            # If the new state has not been explored or added to the frontier, add it to the frontier and path dictionary.
            if new_state not in explored and new_state not in frontier:
                frontier.append(new_state)
                path[new_state] = state


def print_solution(path: dict, state: Tuple[int, int, int]) -> None:
    """Print the solution path from the initial state to the goal state."""
    solution = []
    while state:
        solution.append(state)
        state = path[state]
    solution.reverse()
    for s in solution:
        print_state(s)
    print(f"Solution length: {len(solution)} steps.")


# Test the solution with the initial state.
solve(INITIAL_STATE)
