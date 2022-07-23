# https://iq.opengenus.org/bitwise-division/
def divide(dividend,divisor):

    if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
        Negative_Flag = True
    else:
        Negative_Flag = False

    quotient  = 0
    dividend = abs(dividend)
    divisor = abs(divisor)
    maxLimit = (2**31)-1
    minLimit = -(2**31)
    # print("dividend = ",dividend)

    for i in range(31, -1, -1):
        if (divisor << i) <= dividend:
            print("divisor << i = ",divisor << i)
            dividend -= (divisor << i)
            quotient += 1 << i

    if Negative_Flag:
        quotient = -abs(quotient)

    if quotient >= maxLimit:
        return maxLimit
    elif quotient <= minLimit:
        return minLimit
    else:
        return quotient



dividend = 9999
divisor = 2
print(divide(dividend,divisor))
