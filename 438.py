from collections import Counter


def l438(s, p):
    res = []
    pCounter = Counter(p)
    sCounter = Counter(s[:len(p) - 1])
    print(pCounter, sCounter)
    for i in range(len(p) - 1, len(s)):
        sCounter[s[i]] += 1  # include a new char in the window
        print(sCounter, sCounter, pCounter, sCounter == pCounter)
        if sCounter == pCounter:  # This step is O(1), since there are at most 26 English letters
            res.append(i - len(p) + 1)  # append the starting index
        sCounter[s[i - len(p) + 1]] -= 1  # decrease the count of oldest char in the window
        if sCounter[s[i - len(p) + 1]] == 0:
            del sCounter[s[i - len(p) + 1]]  # remove the count if it is 0
    return res


def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    a = []
    j = len(p)
    pCounter = Counter(p)

    for i in range(len(s) - j + 1):
        if Counter(s[i:i + j]) == pCounter:
            a.append(i)
    return a


print(findAnagrams('cbaebabacd', 'abc'))
# print(l438('cbaebabacd', 'abc'))
