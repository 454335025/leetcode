def l581(nums):
    is_same = [a == b for a, b in zip(nums, sorted(nums))]

    if all(is_same):
        return 0
    else:

        return len(nums) - is_same.index(False) - is_same[::-1].index(False)


print(l581([2, 6, 4, 8, 10, 9, 15]))