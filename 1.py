def l1(nums, target):
    buff_dict = {}
    for i in range(len(nums)):
        print(i,buff_dict)
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[target - nums[i]] = i


print(l1([2, 7, 11, 15], 9))
