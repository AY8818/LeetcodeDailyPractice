def minDistance(word1,word2):
    if len(word1)>len(word2):
        word2,word1=word1,word2
    w1Len = len(word1)
    w2Len = len(word2)
    prev = [0] * (w1Len+1)
    for i in range(w2Len-1,-1,-1):
        curr = [0]* (w1Len+1)
        for j in range(w1Len-1,-1,-1):
            if word1[j] == word2[i]:
                curr[j]= 1+prev[j+1]
            else:
                curr[j] = max(curr[j+1],prev[j])
        prev = curr

    res = w1Len+w2Len - (2*prev[0])
    return res



word1 = 'leetcode'
word2 = 'etco'
print(minDistance(word1,word2))
