def l20(s):
    aa = []
    b = {'}':'{',']':'[',')':'('}
    for value in s:
        if value in b.values():
            aa.append(value)
        elif value in b.keys():
            if aa == [] or b[value] != aa.pop():
                return False
        else:
            return False

    return aa == []

print(l20("()[]{}"))