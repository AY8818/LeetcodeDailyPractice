def isPalindrome(s):
    s = (''.join(c for c in s if c.isalnum())).lower()
    if s == s[::-1]:
        return True
    else:
        return False


s = "race a car"
print(isPalindrome(s))
