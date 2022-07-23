def addBinary(a, b):
    a = a[::-1]
    b = b[::-1]

    if len(a) < len(b):
        a = a + "0" * (len(a) - len(b))
    elif len(b) < len(a):
        b = b + "0" * (len(a) - len(b))

    total = ""
    carry = 0
    for i in range(len(a)):
        bit_sum = (int(a[i]) + int(b[i])) + carry
        if bit_sum == 3:
            total += "1"
            carry = 1
        elif bit_sum == 2:
            total += "0"
            carry = 1
        elif bit_sum == 1:
            total += "1"
            carry = 0
        else:
            total += "0"
            carry = 0
    if carry == 1:
        total += "1"
    return(total[::-1])


a = "11"
b = "1"
print(addBinary(a, b))
