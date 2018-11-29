from collections import Counter
def l169(nums):
    return sorted(nums)[int(len(nums)/2)]
    # return collections.Counter(nums).most_common(1)[0][0]

print(l169([3,2,3]))

