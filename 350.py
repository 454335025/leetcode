from collections import Counter
def l350(nums1,nums2):
    return list((Counter(nums1) & Counter(nums2)).elements())



print(l350([1,2,2,1], [2,2]))