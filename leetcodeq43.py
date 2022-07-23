def plusOne(digits):
    length = len(digits)
    idx = 0
    i = length - 1
    if digits.count(9) == length:
        lst = [0] * (length + 1)
        lst[0] = 1
        return lst
    while True:
        if digits[i] == 9:
            digits[i] = 0
        elif digits[i] != 9:
            idx = i
            break
        i = i - 1
    digits[idx] = digits[idx] + 1

    return digits


digits = [8, 9]
print(plusOne(digits))
