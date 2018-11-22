def l520(s):
    aa = list(s)
    a=0
    b=0
    if ord(aa[0])>=97 and ord(aa[0])<=122:
        for i in range(len(aa)):
            if ord(aa[i])<97:
                return False
    elif ord(aa[0])>=65 and ord(aa[0])<=90:
        for i in range(1,len(aa)):
            if ord(aa[i])<=90:
                a = a+1
            else:
                b=b+1
        if a>0 and b>0:
            return False
    # return s.isupper() or s.islower() or s.istitle()
    return True



print(l520('USa'))