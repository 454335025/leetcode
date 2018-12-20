def l66(digits):

    return list(map(int, list(str(int(''.join(map(lambda x:str(x), digits)))+1))))


print(l66([1,2,3]))
