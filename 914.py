from collections import Counter

def l914(deck):

    a = Counter(deck)
    b = 0
    for i in range(len(a)):
        print(a.most_common()[i][1])
        if b ==0 :
            b = a.most_common()[i][1]
        if a.most_common()[i][1]<2 or b != a.most_common()[i][1]:
            return False
    return True

print(l914([1,1]))