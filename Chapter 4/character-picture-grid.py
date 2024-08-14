grid = [['.', '.', '.', '.', '.', '.'],  # The grid the problem wants me to flip
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for x in range(6):  # Flipping the grid, printing each column on its own row and each row on its own column
    for y in range(8):
        print(grid[y][x],end='')
    print('')
