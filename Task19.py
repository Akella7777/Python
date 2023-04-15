# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.
#
# Input:   [1, 2, 3, 4, 5] k = 3
#
# Output:  [4, 5, 1, 2, 3]

a = [1, 2, 3, 4, 5]
k = int(input())
if k > 0:
    for i in range(k):
       a.insert(0, a.pop())
else:
     for i in range(abs(k)):
       a.append(a.pop(0))
print((a))


# def shift(lst, steps):
#     if steps < 0:
#         steps = abs(steps)
#         for i in range(steps):
#             lst.append(lst.pop(0))
#     else:
#         for i in range(steps):
#             lst.insert(0, lst.pop())
#
#
# nums = [4, 5, 6, 7, 8, 9, 0]
# print(nums)
#
# shift(nums, -2)
# print(nums)
#
# shift(nums, 3)
# print(nums)