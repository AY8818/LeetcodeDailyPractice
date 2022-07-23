def digitSum(s, k):
    length = len(s)
    while length > k:
        lst = []
        for i in range(0, len(s), k):
            lst.append(s[i:i + k])
        new_s = ""
        for strng in lst:
            sublst = list(int(i) for i in strng)
            new_s += str(sum(sublst))
        s = new_s
        length = len(s)
    return s


s = "11111222223"
k = 3
print(digitSum(s, k))
