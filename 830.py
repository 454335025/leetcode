def l830(S):
    aa = []
    i, j, N = 0, 0, len(S)
    while j < N:
        while j < N and S[j] == S[i]: j += 1
        if j - i >= 3: aa.append([i, j - 1])
        i = j

    return aa


print(l830('abcdddeeeeaabbbcd'))
