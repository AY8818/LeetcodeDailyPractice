def largeGroupPositions(s):
    length = len(s)
    if s.count(s[0]) == length:
        if length >= 3:
            return([[0, length - 1]])
        else:
            return([])
    strng = s[0]
    lst = []
    prev_index = 0
    s = s + "$"
    for i in range(length):
        # print(f"\nif {s[i]} == {s[i + 1]} : {s[i] == s[i + 1]}")
        if s[i] == s[i + 1]:
            strng += s[i + 1]
            # print(strng)
        elif s[i] != s[i + 1]:
            # print(strng)
            # print(f"if {len(strng)} >= 3: {len(strng) >= 3}")
            if len(strng) >= 3:
                lst.append([prev_index, i])
                # print(lst)
            strng = s[i + 1]
            prev_index = i + 1

    return lst


s = "aaaabbb"
print(largeGroupPositions(s))
