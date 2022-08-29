# 200. Number of Islands

def numIslands(grid):
    rows, cols = len(grid), len(grid[0])
    islands=0

    def mark(r,c):
        if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]!='1':
            return
        grid[r][c]='0'
        mark(r+1,c)
        mark(r-1,c)
        mark(r,c+1)
        mark(r,c-1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j]=='1':
                mark(i,j)
                islands+=1
    return islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
print(numIslands(grid))

# Problem Description:
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
# return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Constraints:

# a) m == grid.length
# b) n == grid[i].length
# c) 1 <= m, n <= 300
# d) grid[i][j] is '0' or '1'.
