def l28(haystack, needle):
    len_haystack = len(haystack)
    len_needle = len(needle)

    if len_haystack < len_needle:
        return -1

    for i in range(len_haystack - len_needle + 1):
        print(haystack[i:i + len_needle], needle)
        if haystack[i:i + len_needle] == needle:
            return i
    return -1


print(l28('aaaaa', 'bba'))
