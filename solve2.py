from collections import deque

SIZE = 6
GOAL_R = 2
GOAL_C = 5

INITIAL_MULTI = """
002000
002000
112000
000000
000000
000000
"""

INITIAL = INITIAL_MULTI.replace("\n", "")

def toArray(state):
    res = []
    for i in range(0, SIZE * SIZE, 6):
        row = list(state[i: i + 6])
        res.append(row)
    return res

HORZS = "1"
VERTS = "2"
LONGS = "2"
SHORTS = "1"
GOAL_CAR = "1"
EMPTY = "0"
VOID = "X"

queue = deque()
parents = {}

def propose(next, prev):
    if next not in parents:
        parents[next] = prev
        queue.append(next)

def isGoal(state):
    goal_cell = GOAL_R * SIZE + GOAL_C
    if state[goal_cell] == GOAL_CAR:
        return True
    return False

def addNewLines(state):
    out = state[0]
    for i in range(1, len(state)):
        if i % 6 == 0:
            out += '\n' 
        out += state[i]
    return out

def trace(state):
    while state:
        print(addNewLines(state))
        print('\n')
        state = parents[state]

def length(car):
    if car in LONGS:
        return 3
    else:
        return 2

def at(state, row, col):
    if row < 0 or row >= SIZE or col < 0 or col >= SIZE:
        return VOID
    return state[row * SIZE + col]

def countSpaces(state, r, c, dr, dc):
    k = 0
    while at(state, r+k*dr, c+k*dc) == EMPTY:
        k += 1
    return k

def slide(state, r, c, ori, dist, dr, dc, n):
    r += dist * dr
    c += dist * dc
    car = at(state, r, c)
    if car not in ori:
        return
    l = length(car)
    for i in range(n):
        r -= dr
        c -= dc
        nextState = list(state)
        nextState[r * SIZE + c] = car
        nextState[(r+l*dr) * SIZE + (c+l*dc)] = EMPTY
        nextState = ''.join(nextState)
        # nextState = state[:r * SIZE + c] + car + state[r * SIZE + c + 1:]
        # nextState = nextState[:(r+l*dr) * SIZE + (c+l*dc)] + EMPTY + nextState[(r+l*dr) * SIZE + (c+l*dc) + 1:]
        propose(nextState, state)
        state = nextState
        


def explore(state):
    for r in range(SIZE):
        for c in range(SIZE):
            if at(state, r, c) != EMPTY:
                continue
            nU = countSpaces(state, r, c, -1, 0)
            nD = countSpaces(state, r, c, +1, 0)
            nL = countSpaces(state, r, c, 0, -1)
            nR = countSpaces(state, r, c, 0, +1)
            slide(state, r, c, VERTS, nU, -1, 0, nU + nD - 1)
            slide(state, r, c, VERTS, nD, +1, 0, nU + nD - 1)
            slide(state, r, c, HORZS, nL, 0, -1, nL + nR - 1)
            slide(state, r, c, HORZS, nR, 0, +1, nL + nR - 1)
    


def main():
    propose(INITIAL, None)
    solved = False
    while queue:
        current = queue.popleft()
        if isGoal(current) and not solved:
            solved = True
            trace(current)
            break
        explore(current)
    print(f"{len(parents)} explored")

if __name__ == "__main__":
    main()