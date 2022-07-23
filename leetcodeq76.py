def minOperations(nums,x):
    if (nums[0] > x and nums[-1] > x):
            return -1
    noOfSteps = 0
    while True:
        print("\nBegin WHILE LOOP\n")
        print(f"if ({len(nums)} == 0 or {x} <= 0) or ({nums[0]} > {x} and {nums[-1]} > {x}):")
        if (len(nums) == 0 or x <= 0) or (nums[0] > x and nums[-1] > x):
            print("True")
            print("\nEND WHILE LOOP\n")
            break
        else:
            print("False")
        print(f"if {nums[0]} >= {nums[-1]} and {nums[0]}<= {x}:")
        if nums[0] >= nums[-1] and nums[0]<= x:
            print("True")
            print(f"Substract {nums[0]} from {x}")
            x -= nums[0]
            print("x = ",x)
            print(f"Remove {nums[0]} from nums")
            nums.pop(0)
            print("nums = ",nums)
            noOfSteps += 1
        else:
            print("False")
            print(f"Substract {nums[-1]} from {x}")
            x -= nums[-1]
            print("x = ",x)
            print(f"Remove {nums[-1]} from nums")
            nums.pop(-1)
            print("nums = ",nums)
            noOfSteps += 1
        print("noOfSteps = ",noOfSteps)


    if x <= 0:
        return noOfSteps
    else:
        return -1


# nums = [1,1,4,2,3]
# x = 5
# nums = [6016,5483,541,4325,8149,3515,7865,2209,9623,9763,4052,6540,2123,2074,765,7520,4941,5290,5868,6150,6006,6077,2856,7826,9119]
# x = 31841
nums = [5207,5594,477,6938,8010,7606,2356,6349,3970,751,5997,6114,9903,3859,6900,7722,2378,1996,8902,228,4461,90,7321,7893,4879,9987,1146,8177,1073,7254,5088,402,4266,6443,3084,1403,5357,2565,3470,3639,9468,8932,3119,5839,8008,2712,2735,825,4236,3703,2711,530,9630,1521,2174,5027,4833,3483,445,8300,3194,8784,279,3097,1491,9864,4992,6164,2043,5364,9192,9649,9944,7230,7224,585,3722,5628,4833,8379,3967,5649,2554,5828,4331,3547,7847,5433,3394,4968,9983,3540,9224,6216,9665,8070,31,3555,4198,2626,9553,9724,4503,1951,9980,3975,6025,8928,2952,911,3674,6620,3745,6548,4985,5206,5777,1908,6029,2322,2626,2188,5639]
x = 565610


print(minOperations(nums,x))
