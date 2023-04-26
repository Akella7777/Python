# Задача No45.
# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не превосходящее 105
# . Программа должна вывести все пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую пару не дает).
# Ввод: Вывод:
# 300 220 284

k = int(input("Введите натуральное число: "))
a = list()
for i in range(2, k + 1):
    sum = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            sum += j
    a.append([sum, i])
c = list()
for i in range(len(a)):
    for j in range(len(a)):
        if a[i][0] == a[j][1] and a[i][1] == a[j][0] and i != j and a[j] not in c and a[i] not in c: 
            c.append(a[i])
print(c)

# def get_sum(n):
#     s=0
#     for i in range(1,n):
#         if n%i==0:
#             s+=i
#     return s

# def gen_friendlys(n):
#     res=[]
#     for i in range(1,n):
#         if i not in res:
#             tmp=get_sum(i)
#             if i==get_sum(tmp) and i!=tmp:
#                 res.append(i)
#                 res.append(tmp)
#     return res

# print(sum(gen_friendlys(300)))