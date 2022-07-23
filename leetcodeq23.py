def longestIncreasingPath(matrix):
    M, N = len(matrix[0]) - 1, len(matrix) - 1
    # print(f"M= {M} N= {N}")
    visited = []
    for i in range(N + 1):
        visited.append([0] * (M + 1))
    path = 1

    def DFS(n, m):

        if visited[n][m] != 0:
            return visited[n][m]
        temp = 0
        if n != 0 and matrix[n][m] < matrix[n - 1][m]:
            temp = max(temp, DFS(n - 1, m))
        if n != N and matrix[n][m] < matrix[n + 1][m]:
            temp = max(temp, DFS(n + 1, m))
        if m != 0 and matrix[n][m] < matrix[n][m - 1]:
            temp = max(temp, DFS(n, m - 1))
        if m != M and matrix[n][m] < matrix[n][m + 1]:
            temp = max(temp, DFS(n, m + 1))

        visited[n][m] = temp + 1
        return temp + 1

    for i in range(N + 1):
        for j in range(M + 1):
            if visited[i][j] == 0:
                path = max(path, DFS(i, j))

    return path


matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
# matrix = [[1]]
print(longestIncreasingPath(matrix))
