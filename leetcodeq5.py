def maximumGap(nums):
    if len(nums) < 2:
        print("Length is less than 2")
        return 0
    nums.sort()
    print("nums = ", nums)
    maxdiff = 0
    print("Loop begin")
    for i in range(0, len(nums) - 1):
        print("nums[i] = ", nums[i])
        print("nums[i+1] = ", nums[i + 1])
        print(True)
        if nums[i + 1] - nums[i] > maxdiff:
            maxdiff = nums[i + 1] - nums[i]
            print("maxdiff =", maxdiff)
        else:
            print(False)
            continue
    print("End loop ++++++++")
    return maxdiff


nums = [3, 6, 9, 1]
print(maximumGap(nums))
