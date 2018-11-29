from collections import Counter
def l804(words):
    a = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    res = []
    for i in range(len(words)):
        b = ''
        for j in range(len(words[i])):

            b = b + a[ord(words[i][j:j + 1]) - 97]

        res.append(b)

    return len(list(Counter(res)))


print(l804(["gin", "zen", "gig", "msg"]))
