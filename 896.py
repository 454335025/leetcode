def l896(A):
    a = True
    b = True
    for i in range(1,len(A)):
        if A[i]<A[i-1]:
            a = False
        if A[i]>A[i-1]:
            b=False

    return a or b

print(l896([1,3,2]))