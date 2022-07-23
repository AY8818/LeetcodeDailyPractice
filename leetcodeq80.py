def longestStrChain(words):
    words.sort(key=len)
    lst = []
    dp={}
    for word in words:
        lst = []
        for i in range(len(word)):
            print(word[:i]+word[i+1:])
            # print()
            lst.append(dp.get(word[:i] + word[i + 1:], 0)+1)
        print(lst)
        dp[word] = max(lst)
        print(dp)
    return max(dp.values())




words = ["a","b","ba","bca","bda","bdca"]
print(longestStrChain(words))
