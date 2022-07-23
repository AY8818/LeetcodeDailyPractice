def containsNearbyDuplicate(nums,k):
    numDict = {}
    for i,num in enumerate(nums):
        if num in numDict and i - numDict[num] <= k:
            return True
        numDict[num] = i
    return False

nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums,k))
