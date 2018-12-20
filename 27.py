def l27(nums,val):
    a = 0
    for i in range(len(nums)):
        if val != nums[i]:
            nums[a] = nums[i]
            a +=1

    return a
print(l27([3,2,2,3],3))