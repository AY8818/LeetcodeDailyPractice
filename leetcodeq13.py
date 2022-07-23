def mySqrt(x):
    if x == 0 or x == 1:
        return x
    mid = x / 2
    while True:
        mid = int((mid + x / mid) / 2)
        sqr = mid * mid
        sqr2 = (mid + 1) * (mid + 1)
        if sqr == x or (sqr < x and sqr2 > x):
            return mid


x = 25
print(mySqrt(x))
