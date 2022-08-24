# 326. Power of Three

# Solution 1
def isPowerOfThreeSol1(n):
    while n >= 1:
        if n == 1:
            return True
        if n%3:
            return False
        n = n/3
    return False

#Solution 2
# Explanation: The positive divisors of 3 to power 19 are exactly the powers
# of 3 from 30 to 3 to power 19.
# That's all powers of 3 in the possible range here (signed 32-bit integer).
# So just check whether the number is positive and whether it divides 3 to power 19.
def isPowerOfThreeSol2(n):
    return n > 0 == 3**19 % n


n= 27
print(isPowerOfThreeSol1(n))
print(isPowerOfThreeSol2(n))

# Problem Description:
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.

# Example 1:

# Input: n = 27
# Output: true
