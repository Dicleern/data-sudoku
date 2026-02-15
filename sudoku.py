def sudoku_validator(grid):
    for i in range(9):
        row = set()
        column = set()
        box = set()

        for j in range(9):

            if grid[i][j] != 0:
                if grid[i][j] in row: return False
                row.add(grid[i][j])


            if grid[j][i] != 0:
                if grid[j][i] in column: return False
                column.add(grid[j][i])

            row_start = 3 * (i // 3)
            col_start = 3 * (i % 3)


            r = row_start + j // 3
            c = col_start + j % 3

            if grid[r][c] != 0:
                if grid[r][c] in box: return False
                box.add(grid[r][c])

    return True
