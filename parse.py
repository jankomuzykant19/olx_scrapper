import sqlite3

from requests import get

import flat as f
import sites as s

db = sqlite3.connect('data.db')
cursor = db.cursor()

URL = 'https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/lodzkie/'
from bs4 import BeautifulSoup


def create_table():
    cursor.execute('''CREATE TABLE offers (name TEXT, price REAL, city TEXT, size REAL, rooms INT)''')
    quit()


def delete_offers():
    cursor.execute('DELETE from offers;')
    db.commit()


def parse_page(number):
    print(f'Working on page {number}')
    page = get(f'{URL}?page={number}')
    bs = BeautifulSoup(page.content, 'html.parser')
    for offer in bs.find_all('div', class_='offer-wrapper'):  # szukamy divów które mają klasę offer-wrapper
        footer = offer.find('td', class_='bottom-cell')  # w tym jednym divie szukamy td o klasie bottom-cell
        location = footer.find('small', class_='breadcrumb').get_text().strip().split(',')[0]
        # .get_text() wybiera sam tekst // .strip() pozbywa się endl // .split() dzieli stringa kiedy znajdzie
        # przecinek i wybiera [0] czyli pierwsza czesc
        # if location == 'Łódź':               pobieranie dzielnicy
        # district = footer.find('small', class_='breadcrumb').get_text().strip().split(',')[1]
        title = offer.find('strong').get_text().strip()
        price = parse_price(offer.find('p', class_='price').get_text().strip())
        link = offer.find('a')
        link_clear = link['href']
        print(link_clear)
        if s.site_definer(link) == "OLX":
            if "pl/d/" not in link_clear:
                link_clear = link_clear.replace("pl/", "pl/d/")
        size = parse_size(s.site_definer(link), (s.get_size(s.site_definer(link), link_clear)))
        rooms = parse_rooms(s.site_definer(link), (s.get_rooms(s.site_definer(link), link_clear)))
        cursor.execute('INSERT INTO offers VALUES (?, ?, ?, ?, ?)', (title, price, location, size, rooms))
    db.commit()


def get_data_from_db():
    iterator = 0
    flats = []
    for row in cursor.execute('SELECT * FROM offers'):
        flat = f.Flat(row[0], row[1], row[2], row[3], row[4])
        flats.append(flat)
        iterator = iterator + 1
    db.close()
    return flats


def parse_price(price):
    return float(price.replace(' ', '').replace('zł', '').replace(' ', '').replace(',', '.'))


def parse_size(a, size):
    if a == "OLX":
        return float(size.replace('Powierzchnia:', '').replace(' ', '').replace('m²', '').replace(',', '.'))
    if a == "OTODOM":
        return float(size.replace('m²', '').replace(' ', '').replace(',', '.'))


def parse_rooms(a, rooms):
    if a == "OLX":
        return int(
            rooms.replace('Liczba pokoi:', '').replace(' ', '').replace('pokoje', '').replace('pokój', '').replace(
                'iwięcej', ''))
    if a == "OTODOM":
        return int(rooms)
