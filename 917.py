def l917(s):
    i=0
    j = len(s)-1
    S = list(s)
    while i<j:
        while i<j and not S[i].isalpha(): i +=1
        while i<j and not S[j].isalpha(): j -=1
        S[i],S[j] = S[j],S[i]
        i +=1
        j -=1
    return ''.join(S)



print(l917('a-bb-ccc'))
