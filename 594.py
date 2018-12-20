from collections import Counter


def l594(nums):

    l = sorted(list(Counter(nums)))
    s = dict(Counter(nums))
    cnt = 0
    for i in range(len(l)-1):
        if l[i+1] - l[i] ==1:
            cnt = max(cnt,s.get(l[i+1])+s.get(l[i]))
    return cnt


print(l594([1,3,2,2,5,2,3,7]))