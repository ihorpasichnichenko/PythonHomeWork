# Задание 1:
# Запросить у пользователя 5 чисел и записать их в список
#
# a = int(input('Введите первое число...'))
# c = int(input('Введите второе чисел...'))
# d = int(input('Введите третье исел...'))
# e = int(input('Введите четвертое чисел...'))
# f = int(input('Введите пятое чисел...'))
# b = []
# b += a,c,d,e,f
# print(b)
#
#
#
# Задание 2:
# Дан список A = [1, 2, 3, 4, 5]
# Удалить последнее число из списка
#
# A = [1, 2, 3, 4, 5]
# A.remove(5)
# print(A)
#
# Задание 3:
# Запросить у пользователя 10 чисел и записать их в список A
# Запросить у пользователя число N
# Вывести пользователю сколько в списке A повторяется число N
#
# A = []
# b = int(input('Введите число...'))
# c = int(input('Введите число...'))
# d = int(input('Введите число...'))
# e = int(input('Введите число...'))
# f = int(input('Введите число...'))
# g = int(input('Введите число...'))
# l = int(input('Введите число...'))
# m = int(input('Введите число...'))
# n = int(input('Введите число...'))
# o = int(input('Введите число...'))
# N = int(input('Введите число...'))
# A += b,c,d,e,f,g,l,m,n,o
# print(A)
# print(A.count(N))
#
#
#
#
#
# Задание 4:
# Запросить у пользователя число N
# Запросить у пользователя N чисел и записать их в список A
# Вывести список в обратной последовательности
#
#
# A = []
# b = int(input('Введите число...'))
# c = int(input('Введите число...'))
# d = int(input('Введите число...'))
# e = int(input('Введите число...'))
# f = int(input('Введите число...'))
# A += b, c, d, e, f
# print(sorted(A, reverse=True))
#
#
# Задание 5:
# Запросить у пользователя 5 чисел и записать их в список A
# Записать все числа из списка A которые больше 5 в список C
#
# A = []
# C = []
# b = int(input('Введите число...'))
# c = int(input('Введите число...'))
# d = int(input('Введите число...'))
# e = int(input('Введите число...'))
# f = int(input('Введите число...'))
# A += b, c, d, e, f
# for i in A:
#     if i > 5:
#         C.append(i)
#
# print(f'Список A: {A}', f'Список С: {C}')
#
#
#
# Задание 6:
# Запросить у пользователя число N
# Запросить у пользователя N целых чисел и записать их в список A
# Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min, max, sorted, sort).
# Вывести эти числа.
#
# A = []
# for i in range(10):
#     a = int(input('Введите целое число...'))
#     A.append(a)
#
# max = A[0]
# min = A[0]
# for i in A:
#     if max < i:
#         max = i
#     if min > i:
#         min = i
# print(f'Максимальное: {max}' , f'Минимальное: {min}' )
#
#
#
#
#
# Задание 7:
# Пользователь вводит текст нужно вывести количество цифр в этом тексте
#
# A = input()
# digit = 0
# for i in A:
#     if i.isdigit():
#         digit+=1
# if digit == 0:
#     print("Числа в тексте не обнаружены")
# else:
#     print('Количество цифр в тексте - ', digit)
#
#
#
#