def l268(nums):
    nums = sorted(nums)
    for i in range(len(nums)):
        if nums[i] != i:
            return i



print(l268([0,2,1,3,6,5]))