def l463(grid):
    count = 0

    def a(i, j):
        aa = (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)
        b = 0
        for x, y in aa:
            if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[y][x] == 0:
                b += 1
        return b

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[j][i] == 1:
                count += a(i, j)
    return count


print(l463([[0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]]))
