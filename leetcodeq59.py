def hasAllCodes(s,k):
    length = len(s)
    maxSize = 2**k
    if length < (k-1)+maxSize:
        return False
    temp_set = set()
    print(length-k+1)
    for i in range(length-k+1):
        temp_set.add(s[i:i+k])
    return len(temp_set) == maxSize



s = "1101011"
k=2

print(hasAllCodes(s,k))
