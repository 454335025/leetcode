def l788(N):
    b = 0
    for i in range(1, N+1):
        n = str(i)
        if '3' in n or '7' in n or '4' in n:
            continue
        if '2' in n or '5' in n or '6' in n or '9' in n:
            b+=1
    return b


print(l788(10))
