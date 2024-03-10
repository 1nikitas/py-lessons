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
    return BeautifulSoup(request_text,  'html.parser')

def write_data_to_txt(string_: str) -> None:
    with open(f'data_{datetime.now().date()}.txt', 'w', encoding="utf-8") as file:
        file.write(string_)


def get_data(url: str) -> Any:
    '''Отправляет запрос на сайт'''
    request_ = requests.get(url)

    soup = get_soup(request_.text)

    th_s = soup.find_all('th')[:5]
    tr_s = soup.find_all('tr')

    headers = [s.text.strip() for s in th_s]
    string_ = "| " + " | ".join(headers) + " |" + "\n"
    for tr in tr_s:
        td_s = (tr.find_all("td"))[:5]
        for i in range(len(td_s)):
            if i == 0:
                string_ += "| " + td_s[i].text + " |"
            else:
                string_ += td_s[i].text + " |"
        string_ += "\n"

    write_data_to_txt(string_=string_)

get_data(url='https://finance.yahoo.com/currencies/')