# Задача No43
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

size_a = int(input("Введите размер 1 массива: "))
a = list()
for i in range(size_a):
    elem_a = int(input(f"Введите элемент {i+1} для 1 массива: "))
    a.append(elem_a)
print(a)
count = 0
for i in range(size_a):
    for j in range(i + 1, size_a):
        if a[i] == a[j]:
            count += 1
print(count)

# count = 0
# N = int(input('Введите кол-во элементов: '))
# a = []
# for i in range(N):
#     a.append(int(input()))
# print(a)
# for i in range(N):
#     for j in range(i+1, N):
#         if a[i] == a[j]:
#             count += 1
# print(count)