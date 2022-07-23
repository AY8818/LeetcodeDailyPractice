def removeDuplicates(s, k):

    def duplicateChecker(s):
        st = sorted(s)
        for i in range(len(st) - 1):
            if st[i] == st[i + 1]:
                return(True)
            else:
                continue
        return False

    def stringcutter(s, lst):
        slic = False
        print(lst)
        st = ""
        for i in lst:
            print(i[0], i[1])
            if slic == False:
                print(s[i[0]:i[1]])
                st = s[:i[0]] + s[i[1]:]
                slic = True
            elif slic == True:
                print(s[i[0] - k:i[1] - k])
                st = s[:i[0] - k] + s[i[1] - k:]
            print("st =", st)
            s = st
        return st

    def duplicateremover(s, k):
        count = 1
        pos1 = 0
        pos2 = 0
        lst = []
        Flag = False
        print("s = ", s)
        print("LOOP BEGIN ___________")
        for i in range(len(s) - 1):
            print("TOP of Loop======================")
            print("if Flag == True:")
            if Flag == True:
                print("True")
                i = i + 1
                print("Incremented i =", i)
                if i > len(s) - 1:
                    i = len(s) - 1
                    break
            else:
                print("Flag = False")
            print("i = ", i)
            print("s[i] = ", s[i])
            print("s[i+1] = ", s[i + 1])
            if s[i] == s[i + 1]:
                print("True --")
                print("if count == 1")
                if count == 1:
                    print("TRUE count is 1 >>")
                    print("Set pos to ", i)
                    pos1 = i
                else:
                    print("False count != 1 >>")
                count = count + 1
                print("INCREMENT count = ", count)
                print("pos1 = ", pos1)
                print("IF count == k ", count, k)
                if count == k:
                    print(True)
                    count = 1
                    print("Reset Count = ", count)
                    pos2 = i + 1
                    print("pos2 = ", pos2)
                    lst.append([pos1, pos2 + 1])
                    print(lst)
                    Flag = True
                    print("CONTINUE")
                    continue
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                else:
                    print("False Count != k")

            elif s[i] != s[i + 1]:
                print("False i != i+1")
                count = 1
                print("Reset Count = ", count)
                print("CONTINUE")
                print("***********************")
                continue

            print("pos1 = ", pos1)
            print("pos2 = ", pos2)
            print(s[pos1:pos2 + 1])
        return lst

    hasduplicate = duplicateChecker(s)
    if hasduplicate == False:
        return s
    else:
        flag = True
    strng = s

    while len(strng) > k:
        lst = duplicateremover(strng, k)
        strng = stringcutter(strng, lst)
        print("result = ", strng)

    return strng


s = "pbbcggttciiippooaais"
k = 2
print(removeDuplicates(s, k))
