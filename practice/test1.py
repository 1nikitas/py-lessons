# 35000 50000 40000

# [] -- list
# a = [1,2,3,4,5]

#
salaries = [int(i) for i in input().split(" ")] # "35000 50000 40000".split() -> ["35000", "50000", "40000"] -> salaries = [35000, 50000, 40000]
diff = max(salaries) - min(salaries)

max_ = float('-inf')
min_ = float('+inf')

for salary in salaries:
    if salary > max_:
        max_ = salary

    if salary < min_:
        min_ = salary

print('max', max_)
print('min', min_)


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
