# 1996. The Number of Weak Characters in the Game

def numberOfWeakCharacters(properties):
    weakCharacters = 0
    maxDefense = 0
    properties.sort(key = lambda x: (x[0], -x[1]))
    for _, defense in reversed(properties):
        if defense < maxDefense:
            weakCharacters += 1
        else:
            maxDefense = max(maxDefense, defense)

    return weakCharacters
properties = [[5,5],[6,3],[3,6]]
print(numberOfWeakCharacters(properties))

# Problem Description:
# You are playing a game that contains multiple characters, and each of the characters has two
# main properties: attack and defense. You are given a 2D integer array properties where
# properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

# A character is said to be weak if any other character has both attack and defense levels strictly
# greater than this character's attack and defense levels. More formally, a character i is said
# to be weak if there exists another character j where attackj > attacki and defensej > defensei.

# Return the number of weak characters.

# Example 1:
# Input: properties = [[5,5],[6,3],[3,6]]
# Output: 0
# Explanation: No character has strictly greater attack and defense than the other.

# Example 2:
# Input: properties = [[2,2],[3,3]]
# Output: 1
# Explanation: The first character is weak because the second character has a strictly greater
# attack and defense.

# Example 3:
# Input: properties = [[1,5],[10,4],[4,3]]
# Output: 1
# Explanation: The third character is weak because the second character has a strictly greater
# attack and defense.


# Constraints:

# a) 2 <= properties.length <= 105
# b) properties[i].length == 2
# c) 1 <= attacki, defensei <= 105

# Hints:
# Sort the array on the basis of the attack values and group characters with the same attack
# together. How can you use these groups?
