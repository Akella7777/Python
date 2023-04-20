# Задача No25. 
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# ВАРИАНТ 1

print("**********************************")
# s = "aaabcaadcdd"
s = input("Введите строку")
count = dict()
for i in st:
    if i in count:
        count[i] += 1
        print(f"{i}_{count[i]}", end=" ")
    else:
        count[i] = 0
        print(f"{i}", end=" ")



# ВАРИАНТ 2
s = input("Введите строку").split()
dct = {}
for i in s:
    if sym in dct:
        dct[sym] += 1
        print(f"{sym}_{dct[sym]}", end = " ")
        
    else:
        dct[sym] = 0
        print(sym, end = " ")
        