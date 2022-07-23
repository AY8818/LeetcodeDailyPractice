def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    s = strs[0]
    # print("s = ", s)
    for i in range(1, len(strs)):
        # print("i = ", i)
        while strs[i][0:len(s)] != s:
            # print("strs[i] = ", strs[i])
            # print("len(s) = ", len(s))
            # print("strs[i][0:len(s)] = ", strs[i][0:len(s)])
            s = s[0:len(s) - 1]
            # print("s = ", s)
            # print('if len(s) == 0:')
            if len(s) == 0:
                # print(True)
                return ""
    return s


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
