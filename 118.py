def l118(numRows):
    row = [1]
    a = []
    for i in range(numRows):
        a.append(row)
        row =[x + y for x, y in zip([0] + row, row + [0])]

    return a


print(l118(5))
