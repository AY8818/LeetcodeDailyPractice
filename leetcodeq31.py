def hammingDistance(x, y):
    bits = x ^ y
    # print(bits)
    count = 0
    while bits:
        bits = bits & (bits - 1)
        count += 1
    return count


x = 1
y = 4
print(hammingDistance(x, y))
