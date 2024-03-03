"""
Словарь (в Python он называется dict) — ассоциативный массив, изменяемый тип данных, позволяющий,
как и список, хранить много данных. В отличие от списка, в словаре для каждого элемента можно самому определить «индекс»,
по которому он будет доступен.
Этот индекс называется ключом.
"""

"""
    ключ:значение
"""
# a = dict(one=1, wo=2, three=3)
# b = {
#     'one': 1,
#     'two': 2,
#     'three': 3
# }
#
# c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# e = dict({'one': 1, 'three': 3}, two=2)
#
# print(a)
# print(b)
# print(c)
# print(e)
#
# f = {str(k): k for k in range(3)}
# print(f)

gradebook = {"Вася": 5, "Коля": 4, "Петя":2, "Аня": 3}
# print(gradebook)
# print(gradebook["Коля"])
# # print(gradebook[0]) # Ошибка!
# gradebook['Петя'] = 5
# gradebook['Никита'] = 5
# print(gradebook)
#
# # print(gradebook['Маша'])
#
# print(gradebook.get("Маша", "Нет значения!"))

for element in gradebook.keys():
    print(element)

print()

# for element in gradebook.values():
#     print(element)
#
# for element in gradebook.items():
#     print(element[0], element[1])
#
# for name, mark in gradebook.items():
#     print(name, mark)


# print(gradebook.values())
# print(gradebook.keys())
# print(gradebook.items())


# for key in gradebook.keys():
#     print(gradebook[key])

my_dict = {}

# добавляем данные
my_dict[1] = 1
my_dict['hello'] = 'world'

# объединяем элементы списков `students`и `grades` в словарь `gradebook` парами
students = ["Вася", "Коля", "Петя", "Аня"]
grades = [5, 4, 2, 3]
gradebook = list(zip(students, grades))

print(gradebook)

# обновляем словарь, добавляя пары из `gradebook`
my_dict.update(gradebook)
print(my_dict)

gradebook = {"Вася": [
    {
        'name'
    },

    {
        'name'
    },
    {
        'name'
    }
],
    "Коля": 4, "Петя":2, "Аня": 3}
