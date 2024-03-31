import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
import csv

def get_soup(requests_):
    return BeautifulSoup(requests_.text, "html.parser")

def insert_csv(dates):
    with open(f"data-{datetime.now().date()}.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(dates)

def get_data(url):
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
        sql = """INSERT INTO Boxes
    (name, amount, game, price, day, time)
    VALUES(?, ?, ?, ?, ?, ?);
    """
        connection1 = connection(r"D:\SQL db\Steam")
        execute(connection1, sql, dates)
        dates = []

def connection(file):
    '''создание подключения к базе данных'''
    connection = sqlite3.connect(file)
    return connection


def execute(connection, sql, dates):
    '''выполнение запросов'''
    cursor = connection.cursor()
    cursor.executemany(sql, dates)
    connection.commit()


#connection = connection(r"D:\SQL db\Steam")
get_data(f'https://steamcommunity.com/market/search?q=#p1_popular_desc')