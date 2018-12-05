def l643(nums, k):
    a = -10000
    for i in range(len(nums)-k+1):

        a = max(sum(nums[i:i+k]) / k, a)

    return a


print(l643([5], 1))
