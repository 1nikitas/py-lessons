# Задача 2: Подсчет гласных и согласных
# Задача:
# Напишите функцию, которая подсчитывает количество гласных и согласных букв в данной строке.

def count_vowels_consonants(s):
    vowels = "aeiou"
    s = s.lower()  # Приводим к нижнему регистру
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count

# Пример использования
input_str = "Hello, World!"
vowels, consonants = count_vowels_consonants(input_str)
print("Гласные:", vowels)  # Возвращает 3
print("Согласные:", consonants)  # Возвращает 7