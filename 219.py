# 使用字典

# def leetcode219(nums, k):
# for i in range(len(nums) - 1):
#     for j in range(i + 1, len(nums)):
#         if nums[i] == nums[j] and j - i <= k:
#             return True
# return False


def l219(nums, k):
    dic = {}
    for i, v in enumerate(nums):
        print(enumerate(nums),i,v)
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    return False


print(l219([1, 2, 3, 9,1], 10))


# a = {0:11,1:22,2:33,3:44}
# print(a[22])