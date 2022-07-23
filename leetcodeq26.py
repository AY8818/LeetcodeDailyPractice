def removeDuplicates(nums):
    length = 0
    if len(nums) == 0:
        return length
    for i in range(1, len(nums)):
        if nums[length] < nums[i]:
            length += 1
            nums[length] = nums[i]
            print(nums[length])
            print(f"nums[{i}]", nums[i])
            print(nums)
    return length + 1
    # og_len = len(nums)
    # nums = list(dict.fromkeys(nums))

    # k = len(nums)

    # s = og_len - k
    # nums = nums + ([nums[-1] + 1] * s)

    # print(k)
    # # print(nums)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(nums))
