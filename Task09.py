#Задача 9. Решение в группах
#По данному целому неотрицательному n вычислите значение n!.
#N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
#Решить задачу используя цикл while

#Input:       5
#Output:    120

print("Введите число: ")
num = int(input())
factorial = 1
result = 1
while factorial <= num:
    result *= factorial
    factorial += 1
    print(result)
