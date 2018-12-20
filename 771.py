from collections import Counter

def l771(J,S):
    a = 0
    for k,v in Counter(S).items():
        if k in J:
            a +=v

    return a


print(l771('aA','aAAbbbb'))
