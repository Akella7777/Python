# Задача 4:
# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

print("Введеите общее количество журавликов")
a = int(input())
if a > 0:
    if a >= 6:
        Petya = a // 6
        Sergey = a // 6
        Katya = (Petya + Sergey) * 2
        print(f"Петя сделал {Petya}")
        print(f"Сергей сделал {Sergey}")
        print(f"Катя сделал {Katya}")
    else:
        print("Кто то не сделал ни одной фигурки")
else:
    print("Ведено отрицательное число.Введите корректное число")