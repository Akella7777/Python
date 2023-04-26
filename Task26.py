# Задача 26
# Напишите программу, 
# которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

footing = int(input("Введите число А: "))
exponentiation = int(input("Введите в какую степень возводить число А: "))

def Exponentiation (num, exponent):
    if exponent == 0:
        return 1
    else:
        return num * Exponentiation(num, exponent - 1)

number = Exponentiation(footing, exponentiation)
print(number)