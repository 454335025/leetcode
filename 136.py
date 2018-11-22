def l136(nums):
    return 2*sum(set(nums))-sum(nums)

print(l136([1,2,3,2,1]))