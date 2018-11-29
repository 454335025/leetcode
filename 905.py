def l905(A):
    a = []
    b = []
    for aa in A:
        if aa%2==0:
            a.append(aa)
        else :
            b.append(aa)

    return a+b


print(l905([3, 1, 2, 4]))
