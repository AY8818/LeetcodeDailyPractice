def maxProduct(words):
    length = len(words)
    tempSet = [set(words[i]) for i in range(length)] #to get rid of repeated characters in each word
    maxP = 0
    # print(tempSet)
    for i in range(length):
        for j in range(i+1,length):
            # print(not (tempSet[i] & tempSet[j]))
            if not (tempSet[i] & tempSet[j]):
                maxP = max(maxP, len(words[i]) * len(words[j]))

    return maxP



words = ["abcw","baz","foo","bar","xtfn","abcdef"]
words1 = ["a","ab","abc","d","cd","bcd","abcd"]
words2 = ["a","aa","aaa","aaaa"]
print(maxProduct(words))
