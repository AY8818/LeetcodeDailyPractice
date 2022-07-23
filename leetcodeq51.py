def numberOfSteps(num):
    count = 0
    while num != 0:
        if num % 2 == 0:  # num is even
            num = num / 2
        else:
            num = num - 1
        count += 1

    return count


num = 123
print(numberOfSteps(num))
