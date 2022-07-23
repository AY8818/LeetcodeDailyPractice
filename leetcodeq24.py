
def uniquePathsWithObstacles(obstacleGrid):
    x, y = len(obstacleGrid), len(obstacleGrid[0])
    lst = []
    for i in range(x + 1):
        lst.append([0] * (y + 1))
    print(lst)

    lst[0][1] = 1
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if obstacleGrid[i - 1][j - 1] == 0:
                lst[i][j] = lst[i - 1][j] + lst[i][j - 1]

    return lst[-1][-1]


obstacleGrid = [[0, 0], [1, 1], [0, 0]]
obstacleGrid2 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]


print(uniquePathsWithObstacles(obstacleGrid2))
