
''' Импортируем модули '''
from datetime import datetime
import requests

from bs4 import BeautifulSoup
import psycopg2



def get_soup(requests_):
    """Ф-ция извлечение данных из веб-страниц"""
    return BeautifulSoup(requests_.text, "html.parser")


def get_data(url):
    """ Ф-ция для обработки данных и добавления их в БД"""
    request_ = requests.get(url)

    soup = get_soup(request_)
    dives_a = soup.find_all("a",class_="market_listing_row_link")
    dates = []
    for div_a in dives_a:
        name = div_a.find("span",class_="market_listing_item_name").text.strip()
        game = div_a.find("span",class_="market_listing_game_name").text.strip()
        amount = div_a.find("span",class_="market_table_value").text.strip().replace(",","")
        price = div_a.find("span", class_="normal_price").text.strip().split(" ")[1].replace("$","")
        price = price.replace("at:\n", "")
        print(name, game, amount, price, datetime.now().date(), datetime.now().time())
        dates.append([name, int(amount), game, float(price),  str(datetime.now().date()),  str(datetime.now().time())[:8]])
        sql = """INSERT INTO skins
    (id, "name", amount, game, price, "day", "time")
    VALUES(nextval('skins_id_seq'::regclass), %s, %s, %s, %s, %s, %s);
    """
        connection1 = connection("postgresql://gen_user:Jde%25m%3F9P1%40@147.45.107.88:5432/default_db")
        execute(connection1, sql, dates)
        dates = []

def connection(file):
    """ создание подключения к базе данных """
    connection = psycopg2.connect(file)
    return connection


def execute(connection, sql, dates):
    """ выполнение запросов """
    cursor = connection.cursor()
    cursor.executemany(sql, dates)
    connection.commit()

''' Объявление главной функции '''
get_data(f'https://steamcommunity.com/market/search?q=#p1_popular_desc')