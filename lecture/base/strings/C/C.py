# Задача 3: Замена подстроки
# Задача:
# Напишите функцию, которая заменяет все вхождения определенной подстроки в строке на другую подстроку.

def replace_substring(s, old_substring, new_substring):
    return s.replace(old_substring, new_substring)

# Пример использования
input_str = "Hello, World!"
result = replace_substring(input_str, "World", "Python")
print(result)  # Возвращает "Hello, Python!"