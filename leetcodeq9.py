def divide(dividend, divisor):
    # Check if the end result is going to be positive or negative
    sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
    if divisor == -2147483648 and dividend != divisor:
        return 0
    # max limit allowed
    limit = pow(2, 31)
    dividend = abs(dividend)
    divisor = abs(divisor)
    quotient = 0
    current_val = divisor
    coef = 1

    if divisor == 1:
        quotient = dividend
    else:
        while dividend >= divisor:
            if current_val + current_val <= dividend:
                current_val = current_val + current_val
                coef = coef + coef
            else:
                quotient += coef
                dividend -= current_val
                current_val, coef = divisor, 1

    if sign == -1:
        quotient = -quotient

    if quotient > limit - 1:
        return limit - 1
    elif quotient < -limit:
        return -limit

    return quotient


dividend = 2147483647

divisor = 2

print(divide(dividend, divisor))
