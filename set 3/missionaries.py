from collections import deque

def is_valid_state(state):
    missionaries, cannibals, boat_side = state
    if 0 <= missionaries <= 3 and 0 <= cannibals <= 3:
        return missionaries == 0 or missionaries >= cannibals
    return False

def is_goal_state(state):
    return state == (0, 0, 0)

def generate_next_states(state):
    boat_side = state[2]
    next_states = []
    for move_m in range(3):
        for move_c in range(3):
            if move_m + move_c <= 2 and move_m + move_c >= 1:
                new_state = (
                    state[0] - (1 if boat_side == 1 else -1) * move_m,
                    state[1] - (1 if boat_side == 1 else -1) * move_c,
                    1 - boat_side
                )
                if is_valid_state(new_state):
                    next_states.append(new_state)
    return next_states

def bfs():
    start_state = (3, 3, 1)
    visited = set()
    queue = deque([(start_state, [])])
    while queue:
        current_state, path = queue.popleft()
        visited.add(current_state)
        if is_goal_state(current_state):
            return path + [current_state]
        for next_state in generate_next_states(current_state):
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))
    return None

def print_solution_path(path):
    print("Solution Path:")
    for state in path:
        missionaries, cannibals, boat_side = state
        print(f"Missionaries: {missionaries}, Cannibals: {cannibals}, Boat Side: {'Left' if boat_side == 0 else 'Right'}")

def solve_missionaries_cannibals():
    solution_path = bfs()
    if solution_path:
        print_solution_path(solution_path)
    else:
        print("No solution found.")

if __name__ == "__main__":
    solve_missionaries_cannibals()
