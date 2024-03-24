import requests
from bs4 import BeautifulSoup

def get_soup(requests_):
    return BeautifulSoup(requests_.text, "html.parser")

def get_data(url):
    request_ = requests.get(url)

    soup = get_soup(request_)

    dives = soup.find_all("a",class_="market_listing_row_link")

    for div in dives:
        name = div.find("span",class_="market_listing_item_name").text.strip()
        game = div.find("span",class_="market_listing_game_name").text.strip()
        amount = div.find("span",class_="market_table_value").text.strip()
        price = div.find("span", class_="normal_price").text.strip().split(" ")[1]
        price = price.replace("at:\n", "")
        print(name, game, amount, price)

get_data("https://steamcommunity.com/market/search?q=#p1_popular_desc")