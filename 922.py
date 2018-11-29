def l922(A):
    even, odd = [a for a in A if a%2==0], [a for a in A if a % 2 !=0]
    print(even,odd)
    return [even.pop() if  i % 2 == 0 else odd.pop() for i in range(len(A))]


print(l922([4,2,5,7,1,8]))
