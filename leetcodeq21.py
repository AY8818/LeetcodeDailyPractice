def lengthOfLastWord(s):
    w = s.split()
    return len(w[-1])


s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))
