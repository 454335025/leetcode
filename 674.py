def l674(nums):
    a=b=0
    if len(nums) == 1:
        return 1
    for i in range(1,len(nums)):
        if nums[i-1]>=nums[i]:
            a = i
        b = max(b,i-a+1)
    return b

print(l674([1,3,5,4,2,3,4,5]))