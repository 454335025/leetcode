def l448(nums):
    nums = list(set(nums))
    a = []
    print(nums)
    for i in range(len(nums)-1):
        if nums[i+1]-nums[i]>1:
            for j in  range(1,nums[i+1]-nums[i]):
                a.append(nums[i]+j)
            break


    return a

print(l448([4,3,2,7,8,2,3,1]))