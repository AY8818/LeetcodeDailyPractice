def containsDuplicate(nums):
    if len(set(nums)) != len(nums):
        return True
    else:
        return False

nums = [1,2,3,1]
print(containsDuplicate(nums))
