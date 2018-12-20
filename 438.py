from collections import Counter


def l438(s, p):

    l = len(p)
    a = []
    for i in range(len(s)-l):
        print(s[0,1], p)
        exit()
        if s[i,l] == p:
            a.append = i
    return a

print(l438('cbaebabacd', 'abc'))
