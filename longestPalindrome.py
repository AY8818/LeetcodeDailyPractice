def longestPalindrome(s):
    longestPalin = ""
    myDict = {}
    for key,value in enumerate(s):
        # print(key,":",value)
        myDict[value] = myDict.get(value,[]) + [key]
        print(myDict.get(value,[])+ [key])
        for i in myDict.get(value, []):
            print("i = ",i)
            print("key = ",key)
            print(f"if {s[i: key + 1]} == {s[i: key + 1][::-1]}:")
            if s[i: key + 1] == s[i: key + 1][::-1]:
                if len(longestPalin) < len(s[i:key + 1]):
                    longestPalin = s[i:key + 1]
                break


s = "babad"
print(longestPalindrome(s))
