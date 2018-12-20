def l119(rowIndex):
    row = [1]
    for i in range(rowIndex):
        row = [x + y for x, y in zip([0]+row, row+[0])]
        print(row)
    return row


print(l119(10))