def l88(nums1,m,nums2,n):
    return sorted(nums1[:m]+nums2[:n])

print(l88([1,2,3,0,0,0],3,[2,5,6],3))