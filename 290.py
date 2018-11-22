def wordPattern(pattern, str):
    s = pattern
    t = str.split()
    return map(s.find, s) == map(t.index, t)


def l290(pattern, str):
    s = pattern
    t = str.split()
    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)


s = 'abba'
t = 'dog cat cat dog'
t = t.split()
print(t,set(zip(s, t)),set(s),set(t))