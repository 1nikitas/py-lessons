# Задача «Количество нулей»
#
# Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.
# Подсчитайте количество нулей среди введенных чисел и выведите это количество. Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
#
# Sample Input:
# 5
# 0
# 700
# 0
# 200
# 2
# Sample Output:
#
# 2

n = int(input()) # колво чисел
counter_ = 0

for i in range(n):
    x = input()
    count_ = x.count("0")

    if count_:
        counter_ += count_

print(counter_)



# Задача «Потерянная карточка»
# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
#
# Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). Программа должна вывести номер потерянной карточки.
#
# Sample Input:
#
# 5
# 1
# 2
# 3
# 4
# Sample Output:
#
# 5

"""
5
- - - - +
1 2 3 4 5 (n)

sum_ = 1 + 2 + 3 + 4 + 5 = 15

1
2
3
4  (n-1)

sum_n_1 = 1 + 2  + 3 + 4 = 10

sum_ - sum_n_1 = 15 - 10 = 5

"""


a = [int(i) for i in input().split()] # a = list(map(int, input().split()))