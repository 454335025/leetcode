
def l696(s):
    s = map(len, s.replace('01', '0 1').replace('10', '1 0').split())
    for a, b in zip(s, s[1:]):
        print(a,b)
    exit()
    return sum(min(a, b) for a, b in zip(s, s[1:]))


print(l696('00 11 00 11'))
