def runningSum(nums):
    lst = []
    sum = 0
    for i in nums:
        sum += i
        lst.append(sum)
    return lst


nums = [1,2,3,4]
print(runningSum(nums))
