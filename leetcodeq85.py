# 936. Stamping The Sequence
def movesToStamp(stamp, target):
    if stamp == target :
        return [0]
    s = list(stamp)
    t = list(target)
    slen = len(s)
    tlen = len(t) - len(s) + 1
    ans, tdiff, sdiff = [], True, True
    while tdiff:
        tdiff = False
        for i in range(tlen):
            sdiff = False
            for j in range(slen):
                if t[i+j] == "*":
                    continue
                if t[i+j] != s[j]:
                    break
                sdiff = True
            else:
                if sdiff:
                    tdiff = True
                    for j in range(i, i+slen):
                        t[j] = "*"
                    ans.append(i)
    for i in range(len(target)):
        if t[i] != "*":
            return []
    ans.reverse()
    return ans

stamp = "abc"
target = "ababc"
print(movesToStamp(stamp, target))
