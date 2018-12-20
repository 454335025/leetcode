from collections import Counter

def l884(A,B):
    aa = []
    for k,v in dict(Counter(A.split(" "))+Counter(B.split(" "))).items():
        if v == 1:
            aa.append(k)
    return aa




print(l884("this apple is sweet",  "this apple is sour"))