def removeElement(nums, val):
    while True:
        try:
            indx = nums.index(val)
            nums.pop(indx)
        except:
            return len(nums)


nums = [3, 2, 2, 3]
val = 3
print("\n", removeElement(nums, val))
