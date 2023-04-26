# Задача No39.
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 


# size_n = int(input("Введите размер 1 массива: "))
# size_m = int(input("Введите размер 2 массива: "))
# n = set()
# for i in range(size_n):
#     elem_n = int(input(f"Введите элемент {i+1} для 1 массива: "))
#     n.add(elem_n)
# print(n)

# m = set()
# for i in range(size_m):
#     elem_m = int(input(f"Введите элемент {i+1} для 2 массива: "))
#     m.add(elem_m)
# print(m)

# unification = list(set(n.difference(m)))
# unification.sort()
# print(unification)
# for i in unification:
#     print(i, end=' ')








N = int(input("Введите колво элементов 1го массива"))
a = []
for i in range(N):
    a.append(input())
M = int(input("Введите колво элементов 2го массива"))
b = []
for i in range(M):
    b.append(input())
c = []
for i in a:
    if i not in b:
        c.append(i)
print(c)
