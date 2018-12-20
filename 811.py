from collections import Counter


def l811(cpdomains):

    a = {}
    aa = []
    for i in range(len(cpdomains)):
        b = {}
        emails = cpdomains[i].split(' ')

        email = emails[1].split('.')
        for j in range(len(email)):
            b['.'.join(email[j:len(email)])] = int(emails[0])
        a = dict(Counter(a) + Counter(b))

    for i, val in a.items():
        aa.append(str(val) + ' '+i)

    return  aa


print(l811(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
