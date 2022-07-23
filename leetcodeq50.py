def intToRoman(num):
    Roman = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    # print(Roman.keys())
    if num in Roman.keys():
        return Roman[num]
    s = str(num)
    length = len(s)
    output = ""
    if length == 1:
        while num > 0:
            if num >= 1 and num < 4:
                output += "I"
                num -= 1
            elif num >= 5 and num < 9:
                output += "V"
                num -= 5
            elif num == 9:
                return "IX"
            elif num == 4:
                return "IV"
        return output


num = 11
print(intToRoman(num))
