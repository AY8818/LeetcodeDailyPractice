def isPerfectSquare(num):
    l = 0
    r = num
    while l < r:
        print(f"\n({l}+{r})//2 = {(l+r)//2}")
        m = (l+r)//2
        print(m)
        if(m**2 == num):
            return True
        elif(m**2 < num):
            l = m+1
            print("set l= ",l)
        else:
            r = m
            print("set r= ",r)

    if l**2 == num:
        return True
    else:
        return False
    # s = 0
    # i = 1
    # while s<num:
    #     s = i*i
    #     i = i + 1
    # if s == num:
    #     return True
    # else:
    #     return False



num = 10
print(isPerfectSquare(num))
