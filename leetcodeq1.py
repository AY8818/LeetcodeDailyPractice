def searchRange(nums, target: int):
    print([i+2 for i in range(5)])    # lst = []
    # count = 0
    # if target not in nums:
    #     return [-1, -1]

    # for index, num in enumerate(nums):
    #     if num == target:
    #         count = count + 1
    #         if count > 2:
    #             del lst[1]
    #             lst.append(index)
    #         else:
    #             lst.append(index)

    # if len(lst) == 1:
    #     return [lst[0], lst[0]]
    # else:
    #     return lst


nums = [3, 3, 3, 3]
target = 3

output = searchRange(nums, target)

print(output)
