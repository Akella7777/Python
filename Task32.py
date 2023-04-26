# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]


import random

quantity_elem = int(input("Введите количество элементов в массиве N: "))
min_digit = int(input("Введите минимальное число: "))
max_digit = int(input("Введите максимальное число: "))
list = []
list_1 = []
list_2 = []
for i in range(quantity_elem):
    list.append(random.randint(0, max_digit))
print(list)
for i in range(quantity_elem):  
    if list[i] >= min_digit and list[i] <= max_digit:
        list_2.append(list[i])
        list_1.append(i)
print(list_2)
print(list_1)