def l532(nums,k):
    a = []
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if abs(abs(nums[j]) - abs(nums[i]))==k and sorted([nums[i],nums[j]]) not in a:
                a.append(sorted([nums[i],nums[j]]))
    return len(a)


print(l532([-1,1],0))