
def l387(s):
    letters='abcdefghijklmnopqrstuvwxyz'
    index=[s.index(l) for l in letters if s.count(l) == 1]
    print(index)
    return min(index) if len(index) > 0 else -1

print(l387('z'))
