# 1338. Reduce Array Size to The Half
from collections import Counter
def minSetSize(arr):
    length = len(arr)
    lst = [0] * (length+1)
    for i in Counter(arr).values():
        lst[i] += 1

    mid = length // 2
    res = 0
    count = 0
    for i in range(length, -1, -1):
        while lst[i]:
            res += 1
            count += i
            if count >= mid:
                return res
            lst[i] -= 1

    return res
arr = [3,3,3,3,5,5,5,2,2,7]
print(minSetSize(arr))
