-- Создаем таблицу Product
CREATE TABLE Product (
  maker TEXT,
  model TEXT PRIMARY KEY,
  type TEXT
);

-- Создаем таблицу PC
CREATE TABLE PC (
  code TEXT PRIMARY KEY,
  model TEXT REFERENCES Product(model),
  speed INTEGER,
  ram INTEGER,
  hd INTEGER,
  cd TEXT,
  price INTEGER
);

-- Создаем таблицу Laptop
CREATE TABLE Laptop (
  code TEXT PRIMARY KEY,
  model TEXT REFERENCES Product(model),
  speed INTEGER,
  ram INTEGER,
  hd INTEGER,
  price INTEGER,
  screen INTEGER
);

-- Создаем таблицу Printer
CREATE TABLE Printer (
  code TEXT PRIMARY KEY,
  model TEXT REFERENCES Product(model),
  color TEXT,
  type TEXT,
  price INTEGER
);
