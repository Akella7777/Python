# Задача №23.
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2
# Пояснение: (-1 < 5, 2 < 3)

a = [0, -1, 5, 2, 3]
count = 0
for i in (1, len(a)):
    if a[i] > a[i-1]:
        count += 1
print(count)



