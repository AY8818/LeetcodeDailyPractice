# 967. Numbers With Same Consecutive Differences

def numsSameConsecDiff(n, k):
    cur = range(1, 10)
    for i in range(n - 1):
        cur = {(x * 10 + y) for x in cur for y in [x % 10 + k, x % 10 - k] if 0 <= y <= 9}
    return list(cur)

n = 3
k = 7
print(numsSameConsecDiff(n, k))

# Problem Description:
# Return all non-negative integers of length n such that the absolute difference between every two
# consecutive digits is k.
# Note that every number in the answer must not have leading zeros. For example, 01 has one leading
# zero and is invalid. You may return the answer in any order.

# Example 1:
# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.

# Example 2:
# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

# Constraints:
# a) 2 <= n <= 9
# b) 0 <= k <= 9
