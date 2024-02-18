-- Вставляем синтетические данные в таблицу Product
INSERT INTO Product (maker, model, type) VALUES
  ('Manufacturer1', 'Model1', 'PC'),
  ('Manufacturer2', 'Model2', 'Laptop'),
  ('Manufacturer3', 'Model3', 'Printer'),
  ('Manufacturer4', 'Model4', 'PC'),
  ('Manufacturer5', 'Model5', 'Laptop');

-- Вставляем синтетические данные в таблицу PC
INSERT INTO PC (code, model, speed, ram, hd, cd, price) VALUES
  (1, 'Model1', 3000, 8, 500, '4x', 800),
  (2, 'Model2', 2500, 16, 1000, '8x', 1200),
  (3, 'Model3', 2000, 4, 250, '2x', 500),
  (4, 'Model4', 3200, 12, 750, '6x', 1000),
  (5, 'Model5', 1800, 8, 500, '4x', 700);

-- Вставляем синтетические данные в таблицу Laptop
INSERT INTO Laptop (code, model, speed, ram, hd, cd, price, screen) VALUES
  (6, 'Model6', 2200, 12, 750, 'N/A', 1000, 15),
  (7, 'Model7', 2400, 16, 1000, 'N/A', 1200, 17),
  (8, 'Model8', 2000, 8, 500, 'N/A', 800, 14),
  (9, 'Model9', 2600, 32, 1500, 'N/A', 1500, 15),
  (10, 'Model10', 1800, 4, 256, 'N/A', 600, 13);

-- Вставляем синтетические данные в таблицу Printer
INSERT INTO Printer (code, model, color, type, price) VALUES
  (11, 'Model11', 'y', 'Laser', 300),
  (12, 'Model12', 'n', 'Jet', 150),
  (13, 'Model13', 'y', 'Matrix', 200),
  (14, 'Model14', 'n', 'Laser', 250),
  (15, 'Model15', 'y', 'Jet', 180);
