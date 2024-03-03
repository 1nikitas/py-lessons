# 1. Синтаксическая ошибка: Неиспользуемая переменная
#
# Проблема:
#
# В коде объявлена переменная, которая нигде не используется.
# Это может быть признаком недоработки или ошибки в логике программы.

def example_function():
    unused_var = 5
    print("Hello, World!")

# example.py:2:5: F841 local variable 'unused_var' is assigned to but never used