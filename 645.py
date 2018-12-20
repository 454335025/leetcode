from collections import Counter
def l645(nums):
    i = Counter(nums).most_common(1)[0][0]
    if i -1 in set(Counter(nums)):
        return [i,i+1]
    else:
        return [i,i-1]


print(l645([1,2,2,4]))
