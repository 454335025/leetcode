def l832(A):

    for i in range(len(A)):
        a = A[i][::-1]
        for j in range(len(a)):
            A[i][j] = abs(a[j]-1)
    return A


print(l832([[1,1,0],[1,0,1],[0,0,0]]))