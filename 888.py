def l888(A,B):
    a = int((sum(A)-sum(B))/2)
    A = set(A)

    for b in set(B):

        if a+b in A:
            return [a+b,b]


print(l888([1,2,5],[2,4]))