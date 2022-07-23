def removePalindromeSub(s):
    if s[::-1] == s:
        return 1
    return 2


s = "abb"
print(removePalindromeSub(s))
