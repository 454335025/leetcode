def l575(candies):
    return min(len(candies)/2,len(set(candies)))


print(l575([1, 1, 2, 2, 3, 3]))
