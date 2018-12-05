def l189(nums, k):
    n = len(nums)
    k = n%k
    nums[:] = nums[n-k:]+nums[:n-k]
    print(nums)

print(l189([1, 2], 1))
