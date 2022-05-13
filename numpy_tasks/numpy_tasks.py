import numpy as np


def matrix(lines=10, columns=10):
    matr = np.array([[0] * columns for line in range(lines)])
    return matr


def task_10x10():
    lines = 10
    columns = 10
    matr = matrix(lines, columns)
    matr[0][:columns] = 1
    return matr


def task_border(lines=10, columns=10):
    matr = matrix(lines, columns)
    matr[0, :columns] = 1
    matr[lines - 1, :columns] = 1
    matr[1:lines - 1, 0] = 1
    matr[1:lines - 1, columns - 1] = 1
    return matr


def task_2_5x5():
    lines = 5
    columns = 5
    matr = matrix(lines, columns)
    matr[:, :] = 2
    return matr


def task_0123(lines=10, columns=10):  # сомневаюсь, что здесь можно красиво работать с матрицами нечётных размеров
    matr = matrix(lines, columns)
    matr[:lines // 2, columns // 2:columns] = 1
    matr[lines // 2: lines, :columns // 2] = 2
    matr[lines // 2: lines, columns // 2:columns] = 3
    return matr


def task_chess(lines=10, columns=10):
    matr = matrix(lines, columns)
    matr[::2, 1::2] = 1
    matr[1::2, ::2] = 1
    return matr


def task_1_to_9_lines(lines=9, columns=9):
    matr = matrix(lines, columns)
    for line in range(len(matr)):
        matr[line, :] = line + 1
    return matr


def task_1_to_100(lines=10, columns=10):
    matr = matrix(lines, columns)
    num = 1
    for line in range(len(matr)):
        for column in range(len(matr[0])):
            matr[line, column] = num
            num += 1
    return matr


def task_multiplication_table(lines=9, columns=9):
    matr = matrix(lines, columns)
    for line in range(len(matr)):
        matr[line, 0] = line + 1
        for column in range(len(matr[0])):
            matr[line, column] = matr[line, 0] * (column + 1)
    return matr


def task_3_diags(n=4, a=1, b=2):
    matr = matrix(n, n)
    for diag_el in range(n):
        matr[diag_el, diag_el] = a
        if diag_el != 0 and diag_el != n - 1:
            matr[diag_el + 1, diag_el] = b
            matr[diag_el - 1, diag_el] = b
        elif diag_el == 0:
            matr[diag_el + 1, diag_el] = b
        else:
            matr[diag_el - 1, diag_el] = b
    return matr


def task_double_chess(lines=20, columns=20):
    matr = matrix(lines, columns)
    matr[::4, 2::4] = 1
    matr[1::4, 2::4] = 1
    matr[::4, 3::4] = 1
    matr[1::4, 3::4] = 1

    matr[2::4, ::4] = 1
    matr[3::4, ::4] = 1
    matr[2::4, 1::4] = 1
    matr[3::4, 1::4] = 1
    return matr


# the chuck function is WIP
# def chukh(n):
#     matr = matrix(n, n)
#     matr[0, :] =
#     return matr

print(f'task_10x10:\n{task_10x10()}\n')
print(f'task_border:\n{task_border(7, 7)}\n')
print(f'task_2_5x5:\n{task_2_5x5()}\n')
print(f'task_0123:\n{task_0123(8, 8)}\n')
print(f'task_chess:\n{task_chess(6, 4)}\n')
print(f'task_1_to_9_lines:\n{task_1_to_9_lines()}\n')
print(f'task_1_to_100:\n{task_1_to_100()}\n')
print(f'task_multiplication_table:\n{task_multiplication_table(12, 10)}\n')
print(f'task_3_diags:\n{task_3_diags(6, 1, 2)}\n')
print(f'task_double_chess:\n{task_double_chess(22, 22)}\n')
