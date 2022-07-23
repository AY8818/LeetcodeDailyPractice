def isUgly(n):
    if n == 1:
        return True
    prime = [2,3,5]
    for i in range(2,n + 1):
        if n % i == 0:
            count = 1
            for j in range(2,(i//2 + 1)):
                if(i % j == 0):
                    count = 0
                    break
            if(count == 1):
                print(i)
                if i in prime:
                    return True
    return False


n = 14
print(isUgly(n))
