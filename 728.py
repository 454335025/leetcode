def l728(left, right):
    a  = list(range(left, right+1))
    b = []
    for i in a:
        for s in str(i):
            if s == '0' or i %int(s)>0:
                b.append(i)
                break
    return sorted(list(set(a)-set(b)))


print(l728(47, 85))
