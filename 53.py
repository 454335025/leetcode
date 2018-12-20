def l53(nums):



    a = b = nums[0]

    for v in nums[1:]:
        a = max(v,a+v)
        b = max(a,b)
    return b

print(l53([-1,-2,3]))