# Rabbit Leap Problem using BFS and DFS
# Initial state: >>>_<<<
# Goal state: <<<_>>>

from collections import deque

# To check if the goal is reached
def is_goal(state):
    if state == '<<<_>>>':
        return True
    else:
        return False

# To generate all next possible valid states
def get_next_states(state):
    next_states = []
    state = list(state)
    for i in range(7):
        if state[i] == '>':
            # move right
            if i + 1 < 7 and state[i + 1] == '_':
                temp = state[:]
                temp[i], temp[i + 1] = temp[i + 1], temp[i]
                next_states.append(''.join(temp))
            # jump over one rabbit
            if i + 2 < 7 and state[i + 1] in ['<', '>'] and state[i + 2] == '_':
                temp = state[:]
                temp[i], temp[i + 2] = temp[i + 2], temp[i]
                next_states.append(''.join(temp))
        elif state[i] == '<':
            # move left
            if i - 1 >= 0 and state[i - 1] == '_':
                temp = state[:]
                temp[i], temp[i - 1] = temp[i - 1], temp[i]
                next_states.append(''.join(temp))
            # jump over one rabbit
            if i - 2 >= 0 and state[i - 1] in ['<', '>'] and state[i - 2] == '_':
                temp = state[:]
                temp[i], temp[i - 2] = temp[i - 2], temp[i]
                next_states.append(''.join(temp))
    return next_states

# BFS search
def bfs(start):
    queue = deque()
    queue.append((start, [start]))
    visited = set()

    while queue:
        current, path = queue.popleft()

        if is_goal(current):
            return path

        for next_state in get_next_states(current):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    
    return None

# DFS search
def dfs(start):
    stack = []
    stack.append((start, [start]))
    visited = set()

    while stack:
        current, path = stack.pop()

        if is_goal(current):
            return path

        for next_state in reversed(get_next_states(current)):
            if next_state not in visited:
                visited.add(next_state)
                stack.append((next_state, path + [next_state]))
    
    return None

# Initial state of the problem
initial = '>>>_<<<'

# Solve using BFS
print("BFS Solution Path:")
bfs_result = bfs(initial)
for state in bfs_result:
    print(state)

print("DFS Solution Path:")
dfs_result = dfs(initial)
for state in dfs_result:
    print(state)
