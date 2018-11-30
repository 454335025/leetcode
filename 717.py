def l717(bits):
    print()
    return len(bits)%2 !=0 and (''.join(bits[-2:]) !='10' or ''.join(bits[-2:]) !='11')


print(l717([1,1,1,0]))