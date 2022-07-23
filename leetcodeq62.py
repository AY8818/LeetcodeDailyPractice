def isHappy(n):
    temp = set()
    sum =0
    while n != 1:
        for i in str(n):
            sum += int(i)**2
        if sum not in temp:
            temp.add(sum)
        else:
            return False
        n = sum
        sum = 0

    return True
n = 1111111
print(isHappy(n))
