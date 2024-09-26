import numpy as np


def validate(table, row, column, num):
    if num in table[row]:
        return False
    if num in table[:, column]:
        return False
    in_row, in_column = 3 * (row // 3), 3 * (column // 3)
    if num in table[in_row:in_row + 3, in_column:in_column + 3]:
        return False
    return True


def solve_sudoku(table):
    for row in range(9):
        for column in range(9):
            if table[row][column] == 0:
                for num in range(1, 10):
                    if validate(table, row, column, num):
                        table[row][column] = num
                        if solve_sudoku(table):
                            return True
                        table[row][column] = 0
                return False
    return True


def load_sudoku(filename):
    """Carga un Sudoku desde un archivo .txt y lo convierte en una matriz"""
    board = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip().split()
            row = [0 if char == '.' else int(char) for char in row]
            board.append(row)
    return np.array(board)


def display_sudoku(table):
    """Imprime el Sudoku en formato visual"""
    for row in table:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


filename = input('Enter filename: ')
table = load_sudoku(filename)
if solve_sudoku(table):
    print("\nSudoku resuelto:")
    display_sudoku(table)
else:
    print('No se pudo resolver')
