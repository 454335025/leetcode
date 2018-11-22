from collections import Counter
def l383(ransomNote,magazine):
    return not Counter(ransomNote) - Counter(magazine)



print(l383('1234','112233'))

