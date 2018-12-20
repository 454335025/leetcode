def l724(nums):
    aa = sum(nums)
    b = 0
    for i in range(len(nums)):
        if aa - nums[i]-b !=b:
            b +=nums[i]
        else:
            return i

    return -1


print(l724([-1,-1,-1,0,1,1]))