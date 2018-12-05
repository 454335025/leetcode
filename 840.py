def l840(grid):
    a=0
    for i in range(len(grid[0]) - 2):
        for j in range(len(grid) - 2):

            if sum(grid[j]) == sum(grid[j+1]) == sum(grid[j+2]) == grid[j][i] + grid[j + 1][i] +grid[
                j + 2][i] == grid[j][i + 1] + grid[j + 1][i + 1] + grid[j + 2][i + 1] == grid[j][i + 2] +grid[
                        j + 1][i + 2] + grid[j + 2][i + 2] ==  grid[j][i] + grid[j+1][i + 1] + grid[j+2][i + 2] == grid[j][i+2] + grid[j+1][i + 1] + grid[j+2][i]:
                a +=1
    return a

print(l840([
    [10,3,5],
    [1,6,11],
    [7,9,2]]))