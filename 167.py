def l167(numbers,target):
    a = {}

    for i,val in enumerate(numbers):
        if target-val in a:
            return [a[target-val]+1,i+1]

        a[val] = i

print(l167([2,7,11,15],9))