from datetime import datetime
import requests
from bs4 import BeautifulSoup
import psycopg2


def get_soup(url):
    """Fetches and parses HTML content from a URL."""
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")


def extract_data(soup):
    """Extracts product data from parsed HTML content."""
    data = []
    for item in soup.find_all("a", class_="market_listing_row_link"):
        name = item.find("span", class_="market_listing_item_name").text.strip()
        game = item.find("span", class_="market_listing_game_name").text.strip()
        amount = int(item.find("span", class_="market_table_value").text.strip().replace(",", ""))
        price = float(
            item.find("span", class_="normal_price").text.strip().split(" ")[1].replace("$", "").replace("at:\n", "")
        )
        data.append([name, amount, game, price, datetime.now().date(), datetime.now().time().strftime("%H:%M:%S")])
    return data


def insert_data(data, connection):
    """Inserts extracted data into a database table."""
    cursor = connection.cursor()
    sql = """
        INSERT INTO skins (name, amount, game, price, day, time)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.executemany(sql, data)
    connection.commit()


def connect_to_db():
    """Establishes a connection to the database."""
    try:
        connection = psycopg2.connect("postgresql://gen_user:Jde%25m%3F9P1%40@147.45.107.88:5432/default_db")
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


def main():
    """Main function to scrape data and insert into database."""
    url = "https://steamcommunity.com/market/search?q=#p1_popular_desc"
    soup = get_soup(url)
    data = extract_data(soup)

    connection = connect_to_db()
    if connection:
        insert_data(data, connection)
        connection.close()
        print("Data insertion successful.")
    else:
        print("Failed to connect to database.")


if __name__ == "__main__":
    main()
