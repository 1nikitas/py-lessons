# Работа со строками в Python

## Определение строк

Строки в Python представлены неизменяемым типом данных и обозначаются как строка (string). Примеры строк: "abc123", "a".

### Строковые литералы

Строковые литералы - это представление строк в коде, например, "a", "b", "c", "aaa".

### Индексация строк

Индекс элемента - порядковая позиция элемента в строке. Длина строки - от 0 до len(string) - 1.

Пример:
```python
string = "string"
print(string[0])  # первый элемент в наборе
print(string[1])  # второй элемент в наборе
print(string[-1])  # обращение к последнему элементу справа
print(string[len(string) - 1])  # альтернативный способ
```

**Срезы строк**

Срезы позволяют задать начало, конец и шаг индексов для вывода строки.

_Пример:_

```python
string = "string"
print(string[1:6])  # срез с 1 по 5 символ с шагом 1
print(string[1:5:2])  # срез с 1 по 4 символ с шагом 2
print(string[::-1])  # строка наоборот
```
**Сложение строк**

Строки могут быть объединены с использованием оператора "+". Можно также умножать строки на число.

_Пример:_

```python
string1 = "abc"
string2 = "aaa"
print(string1 + string2)  # Конкатенация
print(string1 * 3)  # Умножение
```

**Получение длины строки**

Длину строки можно получить с использованием функции len().

_Пример:_

```python
string1 = "abc"
string2 = "aaa"
print(len(string1) + len(string2))  # Сумма длин строк
```

Поиск подстроки в строке
Метод find() позволяет искать подстроку в строке. Если элемент присутствует, возвращается номер первого вхождения, иначе -1.

_Пример:_

```python
string_ = "aaabbbccc"
print(string_.find("aaa", 0, len(string_) - 1))  # Находит первое вхождение "aaa"
print(string_.find("ddd"))  # Возвращает -1, так как "ddd" отсутствует
```

Метод replace()
Метод replace() используется для замены подстрок в строке.

_Пример:_

```python
string_ = "aaabbbccc"
print(string_.replace('aaa', '###'))  # Заменяет "aaa" на "###"
```
Метод split()
Метод split() разделяет строку на элементы по разделителю.

_Пример:_

```python
string__ = "aaa bbb ccc"
print(string__.split())  # Разбивает строку по пробелу
```
Методы для проверки строк
В Python есть методы для проверки типа символов в строке, такие как isdigit(), isalpha(), islower(), isupper(), isspace().

_Пример:_

``` python
print("5".isdigit())  # Проверка на цифру
print("a".isalpha())  # Проверка на букву
print("a".islower())  # Проверка на нижний регистр
print("A".isupper())  # Проверка на верхний регистр
print(" ".isspace())  # Проверка на пробел
```
Итерация по символам строки
Пример:

```python
string__ = "aaa bbb ccc"
for element in string__:
    print(element.isdigit())  # Проверка на цифру
    print(element.isalpha())  # Проверка на букву
    print(element.islower())  # Проверка на нижний регистр
    print(element.isupper())  # Проверка на верхний регистр
    print(element.isspace())  # Проверка на пробел
    print()
```

## Метод `startswith()` и `endswith()`

Метод `startswith()` используется для проверки, начинается ли строка с определенной подстроки.

_Пример:_

```python
text = "Hello, World!"
print(text.startswith("Hello"))  # Возвращает True
```
Метод endswith() проверяет, заканчивается ли строка определенной подстрокой.

Пример:

```python
text = "Hello, World!"
print(text.endswith("World!"))  # Возвращает True
```
Метод count()
Метод count() возвращает количество вхождений подстроки в строку.

_Пример:_

```python
text = "Python is easy and Python is fun."
print(text.count("Python"))  # Возвращает 2
```
Метод strip(), lstrip(), rstrip()
Метод strip() удаляет пробелы и символы новой строки в начале и конце строки.

_Пример:_

```python
text = "   Hello, World!   "
print(text.strip())  # Возвращает "Hello, World!"
```
Методы lstrip() и rstrip() выполняют аналогичные действия, но только для начала (слева) и конца (справа) строки соответственно.

Метод upper() и lower()
Метод upper() преобразует все символы строки в верхний регистр.

_Пример:_

```python
text = "hello"
print(text.upper())  # Возвращает "HELLO"
```
Метод lower() делает все символы строки строчными.

_Пример:_

```python
text = "HELLO"
print(text.lower())  # Возвращает "hello"
```
Метод join()
Метод join() объединяет элементы последовательности в строку, разделяя их определенным разделителем.

_Пример:_

```python
words = ["Python", "is", "awesome"]
joined_text = " ".join(words)
print(joined_text)  # Возвращает "Python is awesome"
```

Метод format()
Метод format() используется для форматирования строк, вставляя значения переменных в определенные места в строке.

_Пример:_

```python
name = "John"
age = 25
text = "My name is {} and I am {} years old.".format(name, age)
print(text)  # Возвращает "My name is John and I am 25 years old."
```