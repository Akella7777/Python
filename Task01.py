# Задача №1. Общее обсуждение
# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

n = 700
m = 750
print("Введеите количество километров в день")
n = int(input())
print("Введеите количество километров всего маршрута")
m = int(input())

a = ((m+n-1)//n)
print(f"На поездку потребуется дней = {a}")