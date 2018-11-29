from collections import Counter
def l686(A,B):
    print(list(Counter(A).values()))
    return list(Counter(B).values())[0]/list(Counter(A).values())[0]

print(l686('aabbc','aabbcaabb'))
