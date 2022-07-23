def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)

    nums.append(target)
    nums.sort()
    return nums.index(target)


nums = [1, 3, 5, 6]
target = 2
output = searchInsert(nums, target)
print(output)
