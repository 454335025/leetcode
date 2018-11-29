
def l893(A):

    B = set()
    for a in A:
        B.add(''.join(sorted(a[0::2])) + ''.join(sorted(a[1::2])))
    return len(B)

print('abc'[::2])
print(l893(['']))