-- 1) Найдите номер модели, скорость и размер жесткого диска для всех ПК стоимостью менее 500 дол. Вывести: model, speed и h
SELECT PC.code,PC.speed,PC.hd
FROM PC
WHERE PC.price < 500

-- 2) Найдите номер модели, объем памяти и размеры экранов ПК-блокнотов, цена которых превышает 1000 дол.
SELECT code, ram , screen
FROM Laptop
WHERE price > 1000


-- 3) Найдите все записи таблицы Printer для цветных принтеров.
SELECT *
FROM Printer
WHERE color = "y"


-- 4) Найдите номер модели, скорость и размер жесткого диска ПК, имеющих 12x или 24x CD и цену менее 600 дол.
SELECT code, speed, hd
FROM PC
WHERE 	(cd="12x" OR cd="24x") AND
 		price < 600


-- 5) Для каждого производителя, выпускающего ПК-блокноты c объёмом жесткого диска не менее 10 Гбайт, найти скорости таких ПК-блокнотов. Вывод: производитель, скорость.
SELECT p.maker, l.speed
FROM Product p, Laptop l
WHERE 	l.hd > 10 AND
		l.model = p.model