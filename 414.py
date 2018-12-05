from collections import Counter
def l414(nums):
    nums = set(nums)
    print(nums)
    if len(nums)<3:
        return max(nums)
    else:
        return sorted(nums)[-3]

print(l414([3,3,2,1]))