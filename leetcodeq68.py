def isPowerOfTwo(n):
    if n == 0:
        return False

    if n & (n-1) == 0:
        return True
    else:
        return False





n=3
print(isPowerOfTwo(n))
