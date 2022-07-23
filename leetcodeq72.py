def merge(nums1,m,nums2,n):
    nums1[m:] = nums2
    # for i in range(m,len(nums1)):
    #     nums1[i]= nums2[j]
    #     j = j +1
    print("e")
    nums1.sort()
    print(nums1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n  = 3
print(merge(nums1,m,nums2,n))
