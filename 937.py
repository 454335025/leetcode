def l937(logs):
    aa = {}
    for i,log in enumerate(logs):
        log_list = log.split(' ')
        aa[i] = log_list[1]

    print(aa)
    return 1


print(l937(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))