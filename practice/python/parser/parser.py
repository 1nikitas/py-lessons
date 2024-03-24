import csv
from datetime import datetime
from pathlib import Path
from typing import Any

import requests
from bs4 import BeautifulSoup


# TODO: исправить так, чтобы это заработало в рамках файла
# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.com/python/python_file_open.asp
# https://www.w3schools.com/python/python_file_write.asp

# 1. Должен записывать все в рамках файла:
# 2. |Название|Цена|

# Если файл уже существует, то нужно его нужно перезаписать, в остальных случаях создать.
# * https://docs.python.org/3/library/csv.html -- попробовать записать в csv


# TODO:

# 1. Создать таблицу в БД
#       1. raw + tech_changed_dttm(data + time)
#       2. unique (24) + update
# 2. Сделать функции загрузки в бд

# TBD: to be done

# Регулярная загрузка в базу


# proxy: socks5://45.132.177.229:64803:LY8276Wj:cEBtmNNF
#                      ip

#
# http
# https ipv4

#256.256.256.256


def get_soup(request_text: str) -> BeautifulSoup:
    '''Возвращает BeautifulSoup объект'''
    return BeautifulSoup(request_text,  'html.parser')

def write_data_to_txt(string_: str) -> None:
    with open(f'data_{datetime.now().date()}.txt', 'w', encoding="utf-8") as file:
        file.write(string_)

def write_data_to_csv(headers: list, data: list, file_path: Path):
    with open(file_path, 'w', newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)


def get_data(url: str) -> Any:
    '''Отправляет запрос на сайт'''

    proxies = {
        "http": "http://LY8276Wj:cEBtmNNF@45.132.177.229:64803"
    }

    request_ = requests.get(url, proxies=proxies)

    print(request_.text)

    # print(request_.text)
    soup = get_soup(request_.text)

    th_s = soup.find_all('th')[:5]
    tr_s = soup.find_all('tr')

    headers = [s.text.strip() for s in th_s]
    string_ = "| " + " | ".join(headers) + " |" + "\n"
    data = []

    for tr in tr_s:
        td_s = (tr.find_all("td"))[:5]

        string_ += "| " + " | ".join(td.text for td in td_s) + " |\n"
        print('str', string_)
        if td_s:
            row = [td.text for td in td_s]
            print(row)
            data.append(row)
    # print(data)
    # write_data_to_txt(string_=string_)
    write_data_to_csv(headers=headers, data=data, file_path=f'{datetime.now().date()}.csv')

get_data(url='https://finance.yahoo.com/currencies/')


# delimiter ;
# name; age; surname
# 'a'; 23; 'b'