def myPow(x,n):
    print(pow(x,n))
    if n == 0:
      return 1.0
    res = 1
    t = abs(n)
    while t != 0:
        if t%2 == 1:
            res *= x
        t >>= 1
        x = x*x

    if n < 0:
        return 1/res
    else:
        return res



x = 2
n = 3
print(myPow(x,n))
