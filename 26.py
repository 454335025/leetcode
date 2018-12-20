def l26(nums):
    nums[:] = sorted(list(set(nums)))
    return nums


print(l26([1,1,2]))