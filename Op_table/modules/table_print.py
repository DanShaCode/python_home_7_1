import os

def print_operation_table(operation):

    print()
    table = [[1, 2, 3, 4, 5, 6],
    [2, ' ', ' ', ' ', ' ', ' '],
    [3, ' ', ' ', ' ', ' ', ' '],
    [4, ' ', ' ', ' ', ' ', ' '],
    [5, ' ', ' ', ' ', ' ', ' '],
    [6, ' ', ' ', ' ', ' ', ' ']
    ]

    def changer(table):
        for i in range(len(table)):
            for j in range(len(table)):
                if table[i][j] == ' ':
                    table[i][j] = operation(table[i][0],table[0][j])
        return table

    table = changer(table)
    
    for row in table:
        print(*row)
    print()

    user_await = input("Нажмите Enter ")
    os.system('cs||clear')