import random
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


def gen_table():
    table = np.zeros((9, 9), dtype=int)
    for row in range(9):
        for column in range(9):
            if table[row, column] == 0:
                num = random.randint(1, 9)
                if validate(table, row, column, num):
                    if random.random() > 0.5:
                        table[row, column] = num
    return table


def display_sudoku(table):  # Cambié el nombre de la función para evitar conflictos
    for row in table:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


def save_sudoku(table, filename):
    with open(filename, "w") as file:
        for row in table:
            file.write(" ".join(str(num) if num != 0 else '.' for num in row) + "\n")


seed = input('Please set a random combination of number to make a seed: ')
name = input("Enter filename: ")
random.seed(a=seed)
tablero = gen_table()
display_sudoku(tablero)
save_sudoku(tablero, filename=name)
