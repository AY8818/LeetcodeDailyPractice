def combinationSum3(k, n):
    if n < k:
        return []
    elif k == 1 and n == 1:
        return [[1]]
    sublst = []
    mainlst = []
    for i in range(1, 10):
        pass


k = 3
n = 9

print(combinationSum3(k, n))
