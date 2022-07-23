def longestPalindrome(s):
    mydict = {}
    output = ""

    for value, key in enumerate(s):
        print("-------------TOP--------------")
        print("key = ", key)
        print("value = ", value)
        print("mydict = ", mydict)

        mydict[key] = mydict.get(key, []) + [value]
        print(mydict)
        print("mydict[key] value is= ", mydict[key])
        print("\nmydict.get(key, []) = ", mydict.get(key, []))

        print("\n For loop begin ---")
        for i in mydict.get(key, []):
            print("i = ", i)
            #print("if s[i: key + 1] {} == {}{}".format(s[i: key + 1], s[i: key + 1][::-1]))
            print("s[i: value + 1] = ", s[i: value + 1])
            print("s[i: value + 1][::-1] = ", s[i: value + 1][::-1])
            print("\n if s[i: value + 1] == s[i: value + 1][::-1]:")
            if s[i: value + 1] == s[i: value + 1][::-1]:
                print("True\n")
                print("if len(output) < len(s[i:value + 1]):")
                if len(output) < len(s[i:value + 1]):
                    print("True")
                    output = s[i:value + 1]
                    print("output = ", output)
                else:
                    print("False")
                print("\nxxxx BREAk LOOP \n")
                break
            else:
                print("False\n")

    return output


s = "forgeeksskeegfor"

print(longestPalindrome(s))
