from collections import deque
def maximumUniqueSubarray(nums):
    queue = deque([])
    subSet = set()
    setSum = 0
    maxSum = 0
    for i in nums:
        if i not in subSet:
            queue.append(i)
            subSet.add(i)
            setSum += i
        else:
            while queue[0] != i:
                popped = queue.popleft()
                subSet.discard(popped)
                setSum -= popped
            queue.popleft()
            queue.append(i)
        maxSum = max(setSum,maxSum)

    return maxSum



nums =  [187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]
# nums = [5,2,1,2,5,2,1,2,5]
print(maximumUniqueSubarray(nums))
