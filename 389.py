from collections import Counter
def l389(s,t):
    return list(Counter(t)-Counter(s))[0]


print(l389('abcd','abcde'))