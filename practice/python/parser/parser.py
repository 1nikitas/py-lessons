from typing import Any

import requests
from bs4 import BeautifulSoup
from datetime import datetime


# TODO: исправить так, чтобы это заработало в рамках файла
# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.com/python/python_file_open.asp
# https://www.w3schools.com/python/python_file_write.asp

# 1. Должен записывать все в рамках файла:
# 2. |Название|Цена|

# Если файл уже существует, то нужно его нужно перезаписать, в остальных случаях создать.
# * https://docs.python.org/3/library/csv.html -- попробовать записать в csv



def get_soup(request_text: str) -> BeautifulSoup:
    '''Возвращает BeautifulSoup объект'''
    return BeautifulSoup(request_text, 'lxml')

def write_data_to_txt(string_: str) -> None:
    with open(f'data_{datetime.now().date()}.txt', 'w') as file:
        file.write(string_)

def get_data(url: str) -> Any:
    '''Отправляет запрос на сайт'''
    request_ = requests.get(url)

    soup = get_soup(request_.text)

    th_s = soup.find_all('th')
    tr_s = soup.find_all('tr')

    headers = [s.text.strip() for s in soup.find_all('th')][:5]
    print(" ".join(headers))
    write_data_to_txt(string_=" ".join(headers))

    for th in th_s:
        for tr in tr_s:

            for td in tr.find_all('td'):
                # print(td.text, sep=" ", end=' ')
                write_data_to_txt(string_=td.text)
            print()


get_data(url='https://finance.yahoo.com/currencies/')