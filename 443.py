from collections import Counter


def l443(chars):
    aa = []
    j = 1
    for i in range(len(chars) - 1):
        print(chars[i], chars[i+1],j)
        if chars[i] != chars[i+1]:
            aa.append(chars[i])
            if j > 1:
                if j < 10:
                    aa.append(j)
                else:
                    for c in list(str(j)):
                        aa.append(c)
            j = 1

        else:
            j = j + 1

    return aa



print(l443(["a","a","b","b","c","c","c"]))
