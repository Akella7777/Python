# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
# 5
#     1 2 3 4 5
#     3
# -> 1

import random

quantity_elem = int(input("Введите количество элементов в массиве N: "))
max_elem = int(input("Введите максимальное число в массиве: "))
list = []
number = int(input(f"Введите искомое число: "))
count = 0
for i in range(quantity_elem):
    list.append(random.randint(0, max_elem))
    
if number <= max_elem:
    for i in range(quantity_elem):
        if int(list[i]) == number:
            count += 1
    print(list)
    print(f"Искомое число встречается {count} раз")
else:
    print(f"Введено число больше {max_elem}. Введите корректное число")