def l67(a,b):
    c = ''
    len_a = len(a)
    len_b = len(b)
    if len_a-len_b >=0:
        n = len_a
    else:
        n = len_b
    d = 0
    for i in range(n):

        if a[i]+b[i]+d <2:
            c[i] = a[i]+b[i]+d
        elif a[i]+b[i]+d == 2:
            c[i] = 0
            d = 1
        else:
            c[i] =1
            d = 1




a='a'
b= 'bb'
print((a,b))