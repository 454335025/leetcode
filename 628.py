def l628(nums):
    nums = sorted(nums)
    a = nums[-3:]
    b = nums[:2] + nums[-1:]

    return max(a[0]*a[1]*a[2],b[0]*b[1]*b[2])


print(l628([1, 2, 3, 4]))
