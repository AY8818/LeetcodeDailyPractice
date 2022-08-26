 # 869. Reordered Power of 2

 # Solution 1:
def reorderedPowerOf2Sol1(n):
    p2 = set()
    x = 1
    d = len(str(n))
    while True:
        sx = str(x)
        if len(sx) == d:
            srted = sorted(list(sx))
            tpl = tuple(srted)
            p2.add(tpl)
        elif len(sx) > d:
            break
        x *= 2
    srtedn = sorted(list(str(n)))
    tpln = tuple(srtedn)
    return tpln in p2

 # Solution 2:
from collections import Counter
def reorderedPowerOf2Sol2(n):
    c = Counter(str(n))
    return any(c == Counter(str(1 << i)) for i in range(30))

n= 10
print(reorderedPowerOf2Sol1(n))
print(reorderedPowerOf2Sol2(n))

# Problem Description:
# You are given an integer n. We reorder the digits in any order (including the original order)
# such that the leading digit is not zero.
# Return true if and only if we can do this so that the resulting number is a power of two.

# Example 1:
# Input: n = 1
# Output: true

# Example 2:
# Input: n = 10
# Output: false

# Constraints:
# 1 <= n <= 109
