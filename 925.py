def l925(name, typed):
    i,j=0,0
    l1,l2=len(name),len(typed)
    while i<l1 and j<l2:
        if name[i] == typed[j]:
            i,j=i+1,j+1
        elif typed[j] == typed[j-1]:
            j+=1
        else:
            return False
    return True if i==l1 else False



print(l925('leelee','lleeelee'))