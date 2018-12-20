def l747(nums):
    a = max(nums)
    for i in range(len(nums)):
        if nums[i]!=a  and a/2 < nums[i] != 0:
            return -1

    return nums.index(a)


print(l747([1,2,16,35,44,100,27,0]))
