def sudoku_solved(sudoku):
    
    square_rows = {}

    for row in sudoku:
        if len(set(row)) < 9:
            return False
    for column in zip(*sudoku):
        if len(set(column)) < 9:
            return False
    
    for i in range(3):
        square_rows = []
        for row in sudoku:
            square_rows += row[i*3:i*3+3]
            if len(square_rows) == 9:
                if len(set(square_rows)) < 9:
                    return False
                square_rows = []
    return True



print(sudoku_solved([
[4, 5, 2, 3, 8, 9, 7, 1, 6],
[3, 8, 7, 4, 6, 1, 2, 9, 5],
[6, 1, 9, 2, 5, 7, 3, 4 ,8],
[9, 3, 5, 1, 2, 6, 8, 7, 4],
[7, 6, 4, 9, 3, 8, 5, 2, 1],
[1, 2, 8, 5, 7, 4, 6, 3, 9],
[5, 7, 1, 8, 9, 2, 4, 6, 3],
[8, 9, 6, 7, 4, 3, 1, 5 ,2],
[2, 4, 3, 6, 1, 5, 9, 8, 7]
]))
