
def singleNumber(nums):
    length = len(nums)
    if length == 1:
        return nums[0]
    for i in nums:
        if nums.count(i) == 1:
            return i

nums = [2,2,1]
print(singleNumber(nums))
