# Задача 6:
# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

print("Введеите номер билета (целое шестизначное число):")
numberTicket = int(input())
if 99999 < numberTicket < 1000000:
    firstThreeNumber = numberTicket // 1000
    num1 = firstThreeNumber % 10
    firstThreeNumber = firstThreeNumber // 10
    num2 = firstThreeNumber % 10
    firstThreeNumber = firstThreeNumber // 10
    num3 = firstThreeNumber % 10
    res_1 = num1 + num2 + num3
    
    lastThreeNumber = numberTicket % 1000
    num4 = lastThreeNumber % 10
    lastThreeNumber = lastThreeNumber // 10
    num5 = lastThreeNumber % 10
    lastThreeNumber = lastThreeNumber // 10
    num6 = lastThreeNumber % 10
    res_2 = num4 + num5 + num6
    if res_1 == res_2:
        print(f"билет с номером {numberTicket} – счастливый")
    else:
        print(f"билет с номером {numberTicket} – НЕ счастливый")
else:
    print("Введено не шестизначное число. Введите корретное число.")