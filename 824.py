def l824(S):
    a = ['a','A', 'e','E', 'i','I', 'o','O', 'u','U']
    Slist = S.split(' ')
    for i in range(len(Slist)):

        if Slist[i][0] not in a:
            Slist[i] = Slist[i][1:]+Slist[i][0]

        Slist[i] = Slist[i] + 'ma'

    return ''.join(Slist)


print(l824('I speak Goat Latin'))
