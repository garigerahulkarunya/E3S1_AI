from collections import deque

times = {
    "Amogh": 5,
    "Ameya": 10,
    "Grandmother": 20,
    "Grandfather": 25
}

# Initial state
initial_state = (frozenset(["Amogh", "Ameya", "Grandmother", "Grandfather"]), frozenset(), 'L', 0)

# Goal check
def is_goal(state):
    return len(state[0]) == 0 and state[2] == 'R' and state[3] <= 60

# Generate next states
def get_next_states(state):
    left, right, umbrella_side, time_spent = state
    next_states = []

    if umbrella_side == 'L':
        for a in left:
            for b in left:
                if a < b:
                    new_left = left - {a, b}
                    new_right = right | {a, b}
                    time = max(times[a], times[b])
                    next_states.append((new_left, new_right, 'R', time_spent + time))
    else:
        for a in right:
            new_left = left | {a}
            new_right = right - {a}
            time = times[a]
            next_states.append((new_left, new_right, 'L', time_spent + time))

    return next_states

def bfs():
    visited = set()
    queue = deque([(initial_state, [])])
    while queue:
        state, path = queue.popleft()
        if is_goal(state):
            return path + [state]
        if (state[0], state[1], state[2]) not in visited:
            visited.add((state[0], state[1], state[2]))
            for next_state in get_next_states(state):
                if next_state[3] <= 60:
                    queue.append((next_state, path + [state]))
    return None

solution = bfs()

if solution:
    print("Solution found within 60 minutes:\n")
    for step in solution:
        left, right, side, time = step
        print(f"Left: {left} | Right: {right} | Umbrella: {side} | Time: {time} min")
    print(f"\nTotal Time: {solution[-1][3]} minutes")
else:
    print("No solution found within 60 minutes.")
