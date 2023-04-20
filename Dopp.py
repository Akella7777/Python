# Задача 1
# Напишите программу, которая вычисляет двойной факториал натурального числа N ( 1 ≤ N ≤ 10000 ), сохранив все значащие цифры. 
# Двойным факториалом N !! называется произведение натуральных чисел через одно от 1 (для нечётного числа) или от 2 (для чётного числа) 
# до N : N !! = 1·3·5... ( N - 2)· N , если N – нечётное и N !! = 2·4·6... ( N - 2)· N , если N – чётное.

# Входные данные
# Входная строка содержит натуральное число N ( 1 ≤ N ≤ 10000 ).
# Выходные данные
# Программа должна вывести двойной факториал числа N .
# Примеры
# входные данные
# 7
# выходные данные
# 105
# входные данные
# 8
# выходные данные
# 384

print("Введите число: ")
num = int(input())
factorial = 1
if num % 2 == 0:
    for i in range(2, num+1, 2):
        factorial *= i
        print(factorial)
else:
    for i in range(1, num+1, 2):
        factorial *= i
        print(factorial)
print(f"N!!={factorial}")        





# Задача 2
# Напишите программу, которая выводит все цифры, встречающиеся в символьной строке больше одного раза.

# Входные данные
# Входная строка может содержать содержит цифры, пробелы и латинские буквы.

# Выходные данные
# Программа должна вывести в одну строчку в порядке возрастания все цифры, встречающиеся во входной строке больше одного раза. Если таких цифр нет, нужно вывести слово 'NO'.

# Примеры
# входные данные
# asd12gh23
# выходные данные
# 2
# входные данные
# t1y2u3i4o5
# выходные данные
# NO

st_1 = input("Введите первую строку: ")
dig = (0, 1, 2, 3, 4, 5, 6, 7, 8)
count = 0
res = dict()
for i in range(st_1):
    if i in dig:
        count[i] += 1
        print(f"{i}_{count[i]}", end=" ")
    else:
        res[i] += 1
        print(f"{i}", end=" ")



# Задача 3
# Напишите программу, которая находит все символы, встречающиеся в обеих переданных ей строках.

# Входные данные
# На вход программы подаются две символьные строки, каждая строка завершается символом "конец строки".
# Выходные данные
# Программа должна вывести все символы, которые встречаются в обеих строках, в порядке возрастания их ASCII-кодов. Если таких символов нет, нужно вывести слово 'NO'.

# Примеры
# входные данные
# qwerty
# asdqwhy
# выходные данные
# qwy
# входные данные
# qwerty
# 12345
# выходные данные
# NO

# s = "aaabcaadcdd"
# st_1 = input("Введите первую строку: ")
# st_2 = input("Введите вторую строку: ")
# count = dict()
# for i in st_1:
#     for j in st_2:
#         if i == j:
#             count[i] += 1
#             print(f"{i}_{count[i]}", end=" ")
#         else:
#             count[i] = 0
#             print(f"{i}", end=" ")