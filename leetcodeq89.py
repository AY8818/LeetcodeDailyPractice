# 383. Ransom Note

# Solution 1
from collections import Counter
def canConstructSol1(ransomNote, magazine):
    rnDict = Counter(ransomNote)
    magDict = Counter(magazine)

    for key in rnDict.keys():
        if key in magDict and magDict[key] >= rnDict[key]:
            continue
        else:
            return False

    return True


# Solution 2:  we can use set to avoid some duplication. This works amazingly fast
# for the test cases.
def canConstructSol2(ransomNote, magazine):
    return all(ransomNote.count(c)<=magazine.count(c) for c in set(ransomNote))

ransomNote = "aa"
magazine = "aab"
print(canConstructSol1(ransomNote, magazine))
print(canConstructSol2(ransomNote, magazine))

# Problem Description:
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using
# the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Constraints:

# a) 1 <= ransomNote.length, magazine.length <= 105
# b) ransomNote and magazine consist of lowercase English letters.
