from collections import deque

# Check if goal is reached
def is_goal(state):
    return state == '<<<_>>>'

# Generate all valid next moves
def get_next_states(state):
    next_states = []
    state = list(state)
    for i in range(len(state)):
        if state[i] == '>':
            # move right
            if i + 1 < 7 and state[i + 1] == '_':
                new_state = state[:]
                new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
                next_states.append(''.join(new_state))
            # jump over 1 rabbit
            if i + 2 < 7 and state[i + 1] in ('<', '>') and state[i + 2] == '_':
                new_state = state[:]
                new_state[i], new_state[i + 2] = new_state[i + 2], new_state[i]
                next_states.append(''.join(new_state))
        elif state[i] == '<':
            # move left
            if i - 1 >= 0 and state[i - 1] == '_':
                new_state = state[:]
                new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
                next_states.append(''.join(new_state))
            # jump over 1 rabbit
            if i - 2 >= 0 and state[i - 1] in ('<', '>') and state[i - 2] == '_':
                new_state = state[:]
                new_state[i], new_state[i - 2] = new_state[i - 2], new_state[i]
                next_states.append(''.join(new_state))
    return next_states

# Breadth-First Search
def bfs(start):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        state, path = queue.popleft()
        if is_goal(state):
            return path
        for next_state in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    return None

# Depth-First Search
def dfs(start):
    visited = set()
    stack = [(start, [start])]
    while stack:
        state, path = stack.pop()
        if is_goal(state):
            return path
        for next_state in reversed(get_next_states(state)):
            if next_state not in visited:
                visited.add(next_state)
                stack.append((next_state, path + [next_state]))
    return None

# Start the search
initial_state = '>>>_<<<'

print("BFS Solution Path:")
bfs_path = bfs(initial_state)
for step in bfs_path:
    print(step)

print("\nDFS Solution Path:")
dfs_path = dfs(initial_state)
for step in dfs_path:
    print(step)
