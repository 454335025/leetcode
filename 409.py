from collections import Counter


def l409(s):
    odds = 0
    for v in Counter(s).values():
        if v == 1:
            odds+=1

        if v %2 ==1 and v !=1:
            odds+=1

    print(odds)
    return len(s)-odds+bool(odds)


print(l409('abcccccdd'))
