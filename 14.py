def l14(strs):
    if not strs:
        return ""
    shortest = min(strs,key=len)
    print(shortest)
    for i, ch in enumerate(shortest):
        print(i,ch)
        for other in strs:
            print(other,other[i],ch,other[i] != ch)
            if other[i] != ch:
                return shortest[:i]
    return shortest


print(l14(["dog","racecar","car"]))