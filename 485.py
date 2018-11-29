def l485(nums):
    a = 0
    tmp = 0
    for num in nums:
        if num == 0:

            tmp=0
        else:
            tmp+=1
            if a<tmp:
                a= tmp
    return a
print(l485([1,1,0,1,1,1]))