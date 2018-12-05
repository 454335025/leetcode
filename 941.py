def l941(A):
    if len(A)<3:
        return False
    a = max(A)
    l = A.index(a)+1
    print(A[:l] == sorted(set(A[:l])),A[l-1:][::-1] == sorted(set(A[l-1:])))
    return A[:l] == sorted(set(A[:l])) and A[l-1:][::-1] == sorted(set(A[l-1:]))




print(l941([0,3,2,1]))