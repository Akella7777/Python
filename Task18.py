# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
# 5
#     1 2 3 4 5
#     6
# -> 5

import random

quantity_elem = int(input("Введите количество элементов в массиве N: "))
max_elem = int(input("Введите максимальное число в массиве: "))
list = []
number = int(input("Введите число: "))
count = 0
for i in range(quantity_elem):
    list.append(random.randint(0, max_elem))
print(list)

min = abs(list[0] - number)
index = 0

if number <= max_elem:
    for i in range(quantity_elem):
        if list[i] > number:
            min_elem = abs(list[i] - number)
            if min_elem <= min and min_elem != 0:
                min = min_elem
                index = i
    print(f"Ближайщее число к {number} является {list[index]}")
else:
    print(f"Введено число больше {max_elem}. Введите корректное число")


# N = abs(int(input('Введите количество элементов списка А: ')))
# A_entered = input("Введите через пробел элементы списка: ").split()
# A_num = list(map(int, A_entered))
# if len(A_num) != N or N == 0:
#     print('Введенные элементы не соответствуют заявленному количеству!')
# else:
#     X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
#     min = abs(X - A_num[0])
#     index = 0
#     for i in range(1, N):
#         count = abs(X - A_num[i])
#         if count < min:
#             min = count
#             index = i
#     print(f'Число {A_num[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A_num[index])}')