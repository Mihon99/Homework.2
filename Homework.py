# 14: Подсчитать сумму цифр в вещественном числе.

# number = float(input("Введите число: "))

# list = list(str(number).split('.'))

# summ = 0

# for i in list:
#     for j in i:
#         summ += int(j)

# print(f"Сумма цифр в составе числа равна = {summ}")

# 15: Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

# n = int(input("Введите N для набора произведений чисел от 1 до N: "))
# list = [1]
# for i in range(2, n+1):
#     list.append(list[i-2] * i)
# print(f"Полученный набор из призведений чисел {list}")

# 16: Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму
# Пример:
# Для n = 4 {1: 2; 2: 2,25; 3: 2,37; 4 : 2,44}

# n = int(input("Введите число n: "))

# summ = 0

# for i in range(1,n+1):
#     summ += (1+1/i)**i

# print(f"Сумма последовательности (1+1/n)^n = {round(summ, 2)}")

# Задача №17: Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

# import random

# def write_file(numbers):
#     with open('file.txt', 'w') as data:
#         for i in range(numbers):
#             data.write(f"{random.randrange(0, 2*numbers)}\n")

# def read_file():
#     with open('file.txt', 'r') as data:
#         index = list(map(int,data.readlines()))
#     return index

# n = int(input("Введите число N: "))

# numbers = [i for i in range(-n, n+1)]

# write_file(n)

# index = read_file()

# composition = 1

# for i in range(len(index)):
#     composition *= numbers[index[i]]

# print(f"Массив чисел = {numbers}")
# print(f"Массив индексов из файла = {index}")
# print(f"Произведение чисел по заданными файлом инлексами = {composition}")

# 18: Реализовать алгоритм перемешивания списка.

# import random

# list = [random.randint(0,5) for i in range(5)]

# print('Исходный список: ')
# print(list)

# random.shuffle(list)

# print('Список после перемешивания: ')
# print(list)