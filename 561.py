def l561(nums):
    print(sorted(nums)[::2])
    return sum(sorted(nums)[::2])

print(l561([1,4,3,2,10,5]))

