# 1091.Shortest Path in Binary Matrix
from collections import deque


def shortestPathBinaryMatrix(grid):
    grid_len = len(grid)
    if grid[0][0] != 0 or grid[-1][-1] != 0:
        return -1
    coords = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    queue = deque()
    queue.append((0, 0))
    visited = {(0, 0)}

    def neighbours(x, y):
        for x_offset, y_offset in coords:
            new_row = x + x_offset
            new_col = y + y_offset
            if 0 <= new_row < grid_len and 0 <= new_col < grid_len and not grid[new_row][new_col] and (new_row, new_col) not in visited:
                yield (new_row, new_col)

    total = 1
    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()
            if row == grid_len - 1 and col == grid_len - 1:
                return total
            for p in neighbours(row, col):
                visited.add(p)
                queue.append(p)
        total += 1
    return -1


grid = [[0, 1], [1, 0]]
grid2 = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
print(shortestPathBinaryMatrix(grid))
