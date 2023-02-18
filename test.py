import os

operation = lambda x,y: x*y

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