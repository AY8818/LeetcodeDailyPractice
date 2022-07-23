def sortColors(nums):
    for i in range(1,len(nums)):
        val = nums[i]
        j = i-1
        while j>=0 and val<nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1]= val

    return nums



nums = [2,0,2,1,1,0]
print(sortColors(nums))
