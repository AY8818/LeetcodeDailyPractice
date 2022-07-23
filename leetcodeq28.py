def countSubstrings(s):
    # reverse = s[::-1]
    lst = []
    if len(s) == 1:
        return 1

    def checkPalin(strng):
        return strng == strng[::-1]

    count = 0

    for i in range(len(s)):
        x = 0
        y = i
        while y < len(s):
            # print(f"x = {x},y= {y}")
            # print(s[x:y + 1])
            result = checkPalin(s[x:y + 1])
            # print(result)
            # print("-----------------------")
            if result == True:
                count += 1
            y = y + 1
            x = x + 1

    # print(count)

    return count


s = "abaccaba"
print(countSubstrings(s))
