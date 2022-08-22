# 342. Power of Four

def isPowerOfFour(n):
    if n<=0:
        return False
    while n>1:
        if n%4==0:
            n=n//4
        else:
            return False
    return True

n = 16
print(isPowerOfFour(n))


# Problem Description:

# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4x.

# Example 1:
# Input: n = 16
# Output: true
