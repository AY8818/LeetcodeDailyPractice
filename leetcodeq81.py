#34. Find First and Last Position of Element in Sorted Array
def searchRange(nums, target):
    lst = [-1,-1]
    length = len(nums)
    low = 0
    high = length-1

    if (length == 0) or (length == 1 and nums[0] != target):
        return lst

    if nums[0] == target and nums[-1] == target:
        return [0,high]


    while low<=high:
        mid = low + (high-low)//2

        if nums[mid] == target:
            # checking on left side of the mid
            temp = mid
            if nums[0] == target:
                lst[0] = 0
            else:
                lst[0] = mid

                while mid>-1:
                    if nums[mid-1] != target:
                        lst[0] = mid
                        break
                    mid -= 1
            # checking on the right side of the mid
            mid = temp
            if nums[-1] == target:
                lst[1] = length-1
                return lst
            else:
                lst[1] = mid
                while mid<length:
                    if nums[mid] != target:
                        lst[1] = mid-1
                        break
                    mid += 1

            return lst

        elif nums[mid] < target:
            low = mid+1

        elif nums[mid] > target:
            high = mid-1

    return lst
nums = [1,2,3,3,4,5,5,5]
target = 5
print(searchRange(nums, target))
