def l500(words):
    a1 = set('qwertyuiop')
    a2 = set('asdfghjkl')
    a3 = set('zxcvbnm')
    b = []
    for S in words:
        s = set(S.lower())
        if s&a1 == s:
            b.append(S)
        if s&a2 == s:
            b.append(S)
        if s&a3 == s:
            b.append(S)
    return b

print(l500(["Hello", "Alaska", "Dad", "Peace"]))