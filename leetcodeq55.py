def missingNumber(nums):
    max_num= len(nums)
    if max_num not in nums:
        return max_num
    for i in range(0,max_num):
        if i not in nums:
            return i


nums = [3,0,1]
print(missingNumber(nums))
