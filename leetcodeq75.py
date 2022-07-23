def lengthOfLongestSubstring(s):
    subString = ""
    longSubStr = ""
    i = 0
    while i < len(s):
        print(f"\nif {s[i]} not in {subString} :{s[i] not in subString}")
        if s[i] not in subString:
            subString += s[i]
            print("set subString = ",subString)
        elif s[i] in subString:
            print(f"len(subString)> len(longSubStr) : {len(subString)> len(longSubStr)}")
            if len(subString)> len(longSubStr):
                longSubStr = subString
                print("SET longSubStr = ",longSubStr)
            t = subString.index(s[i])
            subString = subString[t+1:]
            print("Reset subString = ",subString)
            print("continue")
            continue

        i += 1
        print("Increment i =",i)

    if len(subString)> len(longSubStr):
        longSubStr = subString
    print("\nlongSubStr = ",longSubStr)
    return len(longSubStr)

s = "dvdf"

print(lengthOfLongestSubstring(s))
