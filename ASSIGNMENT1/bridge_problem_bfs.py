
from collections import deque
times = {
    "Amogh": 5,
    "Ameya": 10,
    "Grandmother": 20,
    "Grandfather": 25
}

initial_state = (frozenset(["Amogh", "Ameya", "Grandmother", "Grandfather"]), frozenset(), 'L', 0)

def is_goal(state):
    left, right, umbrella, total_time = state
    if len(left) == 0 and umbrella == 'R' and total_time <= 60:
        return True
    return False

def get_next_states(state):
    left, right, umbrella_side, time_used = state
    new_states = []

    if umbrella_side == 'L':
    
        for p1 in left:
            for p2 in left:
                if p1 < p2:
                    new_left = left - {p1, p2}
                    new_right = right | {p1, p2}
                    move_time = max(times[p1], times[p2])
                    new_state = (new_left, new_right, 'R', time_used + move_time)
                    new_states.append(new_state)
    else:
        for p in right:
            new_left = left | {p}
            new_right = right - {p}
            move_time = times[p]
            new_state = (new_left, new_right, 'L', time_used + move_time)
            new_states.append(new_state)

    return new_states

def bfs():
    visited = set()
    queue = deque()
    queue.append((initial_state, []))

    while queue:
        current_state, path = queue.popleft()

        if is_goal(current_state):
            return path + [current_state]

        key = (current_state[0], current_state[1], current_state[2])
        if key not in visited:
            visited.add(key)
            next_moves = get_next_states(current_state)
            for new_state in next_moves:
                if new_state[3] <= 60:
                    queue.append((new_state, path + [current_state]))

    return None

result = bfs()

if result:
    print("They can cross the bridge within 60 minutes:\n")
    for step in result:
        left, right, umbrella, time = step
        print(f"Left Side: {left} | Right Side: {right} | Umbrella: {umbrella} | Time Used: {time} min")
    print(f"\nTotal Time Taken: {result[-1][3]} minutes")
else:
    print("It is not possible to cross within 60 minutes.")
