def findMaxForm(strs, m, n):
    # m is zeros
    # n is ones
    subset_count = 0
    for i in strs:
        if i.count("0") <= m and i.count("1") <= n:
            print("valid : ",i)
            subset_count += 1

    return subset_count

# strs = ["10","0001","111001","1","0"]
# m = 5
# n = 3


strs = ["10", "0", "1"]
m = 1
n = 1
print(findMaxForm(strs, m, n))
