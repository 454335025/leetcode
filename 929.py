def l929(emails):
    a = {}
    for i, email in enumerate(emails):
        email_list = email.split('@')
        if '+' in email_list[0]:
            email_list[0] = email_list[0][:email_list[0].find('+')]
        email_list[0] = email_list[0].replace('.','')
        a[email_list[0] + '@' + email_list[1]] = 1

    return len(a)


print(l929(["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
