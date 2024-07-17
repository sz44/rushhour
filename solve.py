from collections import deque


class GridNode:
    def __init__(self, grid, cars, parent, move):
        self.grid = grid
        self.cars = cars
        self.parent = parent
        self.move = move


def solve(grid, cars, player, exit):
    visited = set()

    q = deque([GridNode(grid, cars, None, "")])

    while q:
        node = q.popleft()

        if node.grid[exit[0]][exit[1]] == player:
            return node

        state = grid_to_tuple(node.grid)
        if state in visited:
            continue

        visited.add(state)

        for n, car in node.cars.items():
            if car[2] == "lr":
                # check left
                if car[0][1] > 0 and node.grid[car[0][0]][car[0][1] - 1] == 0:
                    # create new grid
                    new_grid = [row[:] for row in node.grid]
                    new_grid[car[0][0]][car[0][1] - 1] = n
                    new_grid[car[1][0]][car[1][1]] = 0
                    # create new cars obj
                    new_cars = {k: [v[0][:], v[1][:], v[2]] for k, v in node.cars.items()}
                    new_cars[n][0][1] -= 1
                    new_cars[n][1][1] -= 1
                    q.append(GridNode(new_grid, new_cars, node, f"{n}l"))
                    # check right
                if car[1][1] < len(node.grid[0]) - 1 and node.grid[car[1][0]][car[1][1] + 1] == 0:
                    # create new grid
                    new_grid = [row[:] for row in node.grid]
                    new_grid[car[1][0]][car[1][1] + 1] = n
                    new_grid[car[0][0]][car[0][1]] = 0
                    # create new cars obj
                    new_cars = {k: [v[0][:], v[1][:], v[2]] for k, v in node.cars.items()}
                    new_cars[n][0][1] += 1
                    new_cars[n][1][1] += 1
                    q.append(GridNode(new_grid, new_cars, node, f"{n}r"))
            if car[2] == "ud":
                # check up
                if car[0][0] > 0 and node.grid[car[0][0] - 1][car[0][1]] == 0:
                    # create new grid
                    new_grid = [row[:] for row in node.grid]
                    new_grid[car[0][0] - 1][car[0][1]] = n
                    new_grid[car[1][0]][car[1][1]] = 0
                    # create new cars obj
                    new_cars = {k: [v[0][:], v[1][:], v[2]] for k, v in node.cars.items()}
                    new_cars[n][0][0] -= 1
                    new_cars[n][1][0] -= 1
                    q.append(GridNode(new_grid, new_cars, node, f"{n}u"))
                    # check down
                if car[1][0] < len(node.grid) - 1 and node.grid[car[1][0] + 1][car[1][1]] == 0:
                    # create new grid
                    new_grid = [row[:] for row in node.grid]
                    new_grid[car[1][0] + 1][car[1][1]] = n
                    new_grid[car[0][0]][car[0][1]] = 0
                    # create new cars obj
                    new_cars = {k: [v[0][:], v[1][:], v[2]] for k, v in node.cars.items()}
                    new_cars[n][0][0] += 1
                    new_cars[n][1][0] += 1
                    q.append(GridNode(new_grid, new_cars, node, f"{n}d"))


def grid_to_tuple(grid):
    return tuple(tuple(row) for row in grid)


grid = [
    [0, 0, 0],
    [1, 0, 3],
    [0, 2, 0],
]
grid2 = [
    [0, 0, 6, 0],
    [1, 2, 3, 4],
    [0, 0, 5, 0],
    [0, 0, 0, 0],
]
grid3 = [
    [0, 0, 2, 0],
    [1, 1, 2, 3],
    [0, 0, 0, 3],
    [0, 0, 0, 0],
]

cars = {
    1: [[1, 0], [1, 0], 'lr'],
    2: [[2, 1], [2, 1], 'ud'],
    3: [[1, 2], [1, 2], 'ud'],
}
cars2 = {
    1: [[1, 0], [1, 0], 'lr'],
    2: [[1, 1], [1, 1], 'ud'],
    3: [[1, 2], [1, 2], 'ud'],
    4: [[1, 3], [1, 3], 'ud'],
    5: [[2, 2], [2, 2], 'lr'],
    6: [[0, 2], [0, 2], 'lr'],
}
cars3 = {
    1: [[1, 0], [1, 1], 'lr'],
    2: [[0, 2], [1, 2], 'ud'],
    3: [[1, 3], [2, 3], 'ud'],
}


def getMoves(node):
    n = node
    while n:
        print(n.move)
        n = n.parent


a = solve(grid3, cars3, 1, (1, 3))
print(a)
getMoves(a)
