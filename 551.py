def l551(s):
    aa = list(s)
    a = 0
    for i in range(len(aa) - 2):
        if aa[i] == 'A':
            a = a + 1
            if a > 1:
                return False
        elif aa[i] == 'L' and aa[i + 1] == 'L' and aa[i + 2] == 'L':
            return False

    return True


print(l551('PPALLL'))
