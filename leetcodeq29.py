def arrayStringsAreEqual(word1, word2):
    # w1 = "".join(word1)
    if "".join(word1) == "".join(word2):
        return True
    return False


word1 = ["a", "cb"]
word2 = ["ab", "c"]
print(arrayStringsAreEqual(word1, word2))
