def addStrings(num1, num2):
    res = []
    carry = 0
    num1_len = len(num1) - 1
    num2_len = len(num2) - 1

    while num1_len >= 0 or num2_len >= 0 or carry:
        if num1_len >= 0:
            val1 = ord(num1[num1_len]) - ord('0')
        else:
            val1 = 0
        if num2_len >= 0:
            val2 = ord(num2[num2_len]) - ord('0')
        else:
            val2 = 0
        value = (val1 + val2 + carry) % 10
        carry = (val1 + val2 + carry) // 10
        res.append(value)
        num1_len -= 1
        num2_len -= 1

    return ''.join(str(x) for x in res[::-1])


num1 = "456"
num2 = "77"
print(addStrings(num1, num2))
