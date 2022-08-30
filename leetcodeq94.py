# 48. Rotate Image

# Solution 1: The most pythonic solution is a simple one-liner using [::-1]
# to flip the matrix upside down and then zip to transpose it.
def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """

    matrix[:] = zip(*matrix[::-1])



matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)

print(matrix)

# Problem Description:
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Constraints:
# a) n == matrix.length == matrix[i].length
# b) 1 <= n <= 20
# c) -1000 <= matrix[i][j] <= 1000
