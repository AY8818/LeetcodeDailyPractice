def maxSubArray(nums):
    newNum = nums[0]
    maxTotal = nums[0]  
    # print(newNum)      
    
    for i in range(1, len(nums)):
        print(f"newNum = max({nums[i]}, {nums[i]} + {newNum})")
        newNum = max(nums[i], nums[i] + newNum)
        print("newNum = ",newNum) 
        print(f"\nmaxTotal = max({newNum}, {maxTotal})")
        maxTotal = max(newNum, maxTotal)
        print("maxTotal = ",maxTotal,"\n")

    return maxTotal 


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
