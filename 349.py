from collections import Counter
def l349(nums1,nums2):

    return list(Counter(nums1) & Counter(nums2))


print(l349([1,2,2,1],[2,2]))