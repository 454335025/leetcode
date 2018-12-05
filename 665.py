def l665(nums):
    a,b=nums[:],nums[:]


    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            a[i] = nums[i+1]
            b[i+1] = nums[i]
            break


    return a == sorted(a) or b ==sorted(b)





print(l665([2,3,3,2,4]))

