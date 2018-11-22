def l557(s):
    list = s.split()
    a = ''
    for i in range(len(list)):
        a = a + list[i][::-1]+' '
    print(a)



print(l557("Let's take LeetCode contest"))