# 363. Max Sum of Rectangle No Larger Than K

import bisect
def maxSumSubmatrix(matrix, k):
    ans = float("-inf")
    m, n = len(matrix), len(matrix[0])
    for i in range(n):
        lstSum = [0] * m
        for j in range(i, n):
            currSum = 0
            curlstSum = [0]
            for t in range(m):
                lstSum[t] += matrix[t][j]
                currSum += lstSum[t]
                pos = bisect.bisect_left(curlstSum, currSum - k)
                if pos < len(curlstSum):
                    if curlstSum[pos] == currSum - k:
                        return k
                    else:
                        ans = max(ans, currSum - curlstSum[pos])
                bisect.insort(curlstSum, currSum)
    return ans

matrix = [[1,0,1],[0,-2,3]]
k = 2
print(maxSumSubmatrix(matrix, k))

# Problem Description:

# Given an m x n matrix matrix and an integer k, return the max sum of a rectangle
# in the matrix such that its sum is no larger than k.
# It is guaranteed that there will be a rectangle with a sum no larger than k.


# Example 1:
# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2
# Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and
#  2 is the max number no larger than k (k = 2).

# Example 2:
# Input: matrix = [[2,2,-1]], k = 3
# Output: 3

# Constraints:

#a) m == matrix.length
#b) n == matrix[i].length
#c) 1 <= m, n <= 100
#d) -100 <= matrix[i][j] <= 100
#e) -105 <= k <= 105
