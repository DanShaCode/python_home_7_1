import os

# 1. Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6)
# 2. Которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# 3. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,которые должны быть распечатаны. 

def print_operation_table():
    os.system('cs||clear')
    print()
    table = [[1, 2, 3, 4, 5, 6],
    [2, ' ', ' ', ' ', ' ', ' '],
    [3, ' ', ' ', ' ', ' ', ' '],
    [4, ' ', ' ', ' ', ' ', ' '],
    [5, ' ', ' ', ' ', ' ', ' '],
    [6, ' ', ' ', ' ', ' ', ' ']
    ]
    for row in table:
        print(*row)
    print()

    
    user_await = input("Нажмите Enter ")
    os.system('cs||clear')

print_operation_table()