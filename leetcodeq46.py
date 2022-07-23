def hammingWeight(n):
    # count = 0
    # while n:
    #     count += 1

    return bin(n).count("1")


n = 0b11111111111111111111111111111101

print(hammingWeight(n))
