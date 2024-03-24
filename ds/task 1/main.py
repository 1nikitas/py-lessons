import pandas as pd
from zipfile import ZipFile
import os

dataset_ = 'diabetes.csv'
diabetes_data = pd.read_csv(dataset_)

# data_info = diabetes_data.info()
#
# data_head = diabetes_data.head()

# print(data_info)
# print(data_head)

zip_file_path = 'archive (1).zip'

with ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall('.')


correlation = diabetes_data.corr()['Outcome'].sort_values()
# print(correlation)

files = os.listdir()
print(files)

path1 = 'test.csv'
path2 = 'train.csv'
path3 = 'diabetes.csv'

list_of_path = [path1, path2, path3]
csv_data_corrected = {}

# Чтение каждого файла из списка путей и сохранение данных в словарь
for item in list_of_path:
    csv_data_corrected[item] = pd.read_csv(item)
    print(csv_data_corrected[item].info(), csv_data_corrected[item].head())


