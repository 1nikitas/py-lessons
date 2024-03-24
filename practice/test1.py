# 35000 50000 40000

# [] -- list
# a = [1,2,3,4,5]

#
# salaries = [int(i) for i in input().split(" ")] # "35000 50000 40000".split() -> ["35000", "50000", "40000"] -> salaries = [35000, 50000, 40000]
# diff = max(salaries) - min(salaries)
#
# max_ = float('-inf')
# min_ = float('+inf')

# for salary in salaries:
#     if salary > max_:
#         max_ = salary
#
#     if salary < min_:
#         min_ = salary
#
# print('max', max_)
# print('min', min_)
#

# <-------->
# 0        9

# 0 1 2 # range(3)

# range(start, end, step)

# <---->
# 3 ... 9
# 3 +2 = 5
# 5 + 2 = 7

# for i in range(1, 10): # 1
#     for j in range(1, 10): # i = 1
#         for k in range(1, 10):
#             for m in range(1, 10):
#                 print(i, j, k, m)

# 30 - алфавит
# _ _ _ _ _ _ _ - 7 символов
# 30*30 30 30 30 30 30 == 30 ** 7 = 21870000000

# print(30 ** 7)


# list
# iter -- next()

#        0 1 2 . len(list_) - 1
list_ = [1,2,3,4,5]
# print(list_[0])
# print(list_[-1])
# print(list_[len(list_)])

#
# string_ = "string"
# for element in range(len(string_)):
#     print(element, string_[element])
#
# print()
# #
# for element in range(len(list_)):
#     print(element, list_[element])

# print('len', len("string"))

# Задача «Две половинки»
# Дана строка. Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная,
# то длина первой части должна быть на один символ больше).
# Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.
#
# При решении этой задачи не стоит пользоваться инструкцией if.

# 1 8 3 8 4 8 -- МОДА 8
# 1 2 3 4 -- Медиана
# (2 + 3) / 2

# 1 2 3 4 5 -- Медиана
# 3






# n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
# Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке?
# Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).
# n, k = int(input()), int(input())
#
# # Сколько яблок достанется каждому школьнику?
# print(k // n)
# print(k % n)

#
#
# minutes = int(input()) # количество минут сначала суток
# hours = minutes % (24 * 60) // 60
# print(hours)
# print(minutes % 60) # 150 -> 2 30 -> 30 % 60 -> 30

"""
1. ввод данных
2 обработка данных
3 составление алгоритма -> 
4 вывод ответа
"""


# print(100 % 150) # 100
# print(200 % 150) # 200 - 150 = 50
#
# equation = input()
#
# a, b, c = equation.split("+", maxsplit=2)
# c = c.split("=")[0]
#
# a = a.split("x")[0]
# b = b.split('x')[0]
# print(a,b,c)


def sum_after_second_negative(input_str):
    numbers = list(map(int, input_str.split()))
    negative_count = 0
    sum_even = 0
    for num in numbers:
        if num < 0:
            negative_count += 1
            if negative_count == 2:
                continue  # Skip the second negative itself
        if negative_count >= 2:
            if num % 2 == 0:
                sum_even += num
    return sum_even

# Example input
input_str = "3 5 -7 -13 43 8 1 -13 8 -1"
print(sum_after_second_negative(input_str))
