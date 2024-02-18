"""Строки

Неизменяемый тип данных

string – строка (от англ)
"abc123" – string
"a" – string

строковый литерал - "a", "b", "c"
"aaa"

'a' == "a" True
"""

# длина строки - 0 до len(string) - 1

#         01234...len(string)-1
string = "string"

"""
индекс элемента -- порядковая позиция элемента в наборе


"""
print(string[0]) # первый элемент в наборе (самый левый)
print(string[1]) # второй элемент в наборе

print(string[-1]) # обращение к последнему справа элементу
print(string[len(string) - 1])
# print(string[len(string)])

"""
Срезы - это возможность задать начало, конец и шаг индексов для вывода строки.

start - индекс начала
end - индекс конца
step - шаг,

range(5) -> 01234; step = 1
range(1,5,2) -> 13; step = 2

   s e
 012345
"string"
"""

print(string[1:6])
print(string[1:5:2])

# print(string[10])
print(string[::]) # от начала до конца с шагом 1. значения проставляются по умолчанию
print(string[::-1]) # строка наоборот


# сложение строк
string1 = "abc"
string2 = "aaa"

print(string1 + string2) # Конкатенация
print(string1 * 3)

print(string1[0] + string2[0])

# получение длины
print(len(string1) + len(string2)) # 3 + 3

# поиск подстроки в строке
#          0  12345...
#          ___

# если элемент присутствует в строке, то результат: номер первого вхождения
# если элемента нет, то -1
string_ = "aaabbbccc"
print(string_.find("aaa", 0, len(string_) - 1))
print(string_.find("ddd"))

print(string_.find('.'))    # ->
print(string_.rfind('.'))   # <-

# print(string_.index("dd")) ОШИБКА!

print(string_.replace('aaa', '###'))

# def main():
#   a = 5
#   return ... a

# def main1():
#     return 2
#
# def main2():
#     print(1)
#
# value_main1 = main1() # 2
# value_main2 = main2() # None
#
# print(value_main1)
# print(value_main2)

string__ = "aaa bbb ccc"

# split() - метод который разделяет строку на элемент по разделителю
"""
по умолчанию – split() - разбиение по пробелу

"aaa bbb ccc".split() -> ['aaa', 'bbb', 'ccc']
"aaa,bbb,ccc".split(',') -> ['aaa', 'bbb', 'ccc']
"""


print("5".isdigit()) # проверка на цифру
print("a".isalpha()) # проверка на букву
print("a".islower()) # проверка на нижний регистр
print("A".isupper()) # проверка на верхний регистр
print(" ".isspace()) # проверка на пробел


# выводим каждый элемент строки отдельно
for element in string__:
    print(element.isdigit())  # проверка на цифру
    print(element.isalpha())  # проверка на букву
    print(element.islower())  # проверка на нижний регистр
    print(element.isupper())  # проверка на верхний регистр
    print(element.isspace())  # проверка на пробел
    print()