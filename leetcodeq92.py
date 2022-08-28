# 1329. Sort the Matrix Diagonally

def diagonalSort(mat):
    row = len(mat)
    col = len(mat[0])
    print(row,col)
    myDict = defaultdict(list)
    for i in range(row):
        for j in range(col):
            myDict[i - j].append(mat[i][j])

    for key in myDict:
        myDict[key].sort(reverse=1)
    for i in range(row):
        for j in range(col):
            mat[i][j] = myDict[i - j].pop()
    return mat

mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
print(diagonalSort(mat))

# Problem Description:
# A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row
# or leftmost column and going in the bottom-right direction until reaching the matrix's end.
# For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes
# cells mat[2][0], mat[3][1], and mat[4][2].

# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return
# the resulting matrix.

# Example 1:
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

# Constraints:

# a) m == mat.length
# b) n == mat[i].length
# c) 1 <= m, n <= 100
# d) 1 <= mat[i][j] <= 100
