def merge(nums1, m, nums2, n):
    for i in nums2:
        indx = nums1.index(0)
        nums1[indx] = i

    nums1.sort()
    print(nums1)


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(merge(nums1, m, nums2, n))
