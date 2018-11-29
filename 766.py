def l766(matrix):

    for i in range(len(matrix)-1):
        if matrix[i][:-1] != matrix[i+1][1:]:
            return False
    return True


print(l766([
    [1,2,3,4],
    [5,1,2,3],
    [9,5,1,2]
]))