from bs4 import BeautifulSoup
from requests import get


def site_definer(tab):
    if tab['href'][13] == "l":
        return "OLX"
    elif tab['href'][13] == "t":
        return "OTODOM"
    else:
        return "Błąd"


def get_size(a, link):
    if a == "OLX":
        olx_page = get(link)
        bs_olx = BeautifulSoup(olx_page.content, 'html.parser')
        for it in bs_olx.find_all('li', class_='css-ox1ptj'):
            rm = it.find('p', class_='css-xl6fe0-Text eu5v0x0').get_text()
            if "Powierzchnia:" in rm:
                size_olx = rm
        return size_olx

    if a == "OTODOM":
        otodom_page = get(link)
        bs_otodom = BeautifulSoup(otodom_page.content, 'html.parser')
        size_otodom = bs_otodom.find('div', class_='css-1ytkscc ecjfvbm0').get_text()
        return size_otodom


def get_rooms(a, link):
    if a == "OLX":
        olx_page = get(link)
        bs_olx = BeautifulSoup(olx_page.content, 'html.parser')
        for it in bs_olx.find_all('li', class_='css-ox1ptj'):
            rm = it.find('p', class_='css-xl6fe0-Text eu5v0x0').get_text()
            if "Liczba pokoi:" in rm:
                rooms_olx = rm
        return rooms_olx

    if a == "OTODOM":
        otodom_page = get(link)
        bs_otodom = BeautifulSoup(otodom_page.content, 'html.parser')
        rooms_otodom = bs_otodom.find_all('div', class_='css-1ytkscc ecjfvbm0')
        if rooms_otodom[1].get_text().isnumeric():
            return rooms_otodom[1].get_text()
        elif rooms_otodom[2].get_text().isnumeric():
            return rooms_otodom[2].get_text()
        else:
            return rooms_otodom[3].get_text()
