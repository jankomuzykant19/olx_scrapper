from collections import Counter


class Flat:
    def __init__(self, name, price, location, size, rooms):
        self.name = name
        self.price = price
        self.location = location
        self.size = size
        self.rooms = rooms


def average_size_city(city, tab):
    counter = 0
    avg_size = 0
    for x in range(len(tab)):
        if city == tab[x].location:
            avg_size = avg_size + tab[x].size
            counter = counter + 1

    return round(avg_size / counter, 2)


def average_price_city(city, tab):
    counter = 0
    avg_price = 0
    for x in range(len(tab)):
        if city == tab[x].location:
            avg_price = avg_price + tab[x].price
            counter = counter + 1

    return round(avg_price / counter, 2)


def get_all_prices(tab):
    prices = []
    for x in range(len(tab)):
        prices.append(tab[x].price)
    return prices


def get_all_sizes(tab):
    sizes = []
    for x in range(len(tab)):
        sizes.append(tab[x].size)
    return sizes


def get_all_cities(tab):
    cities = []
    for x in range(len(tab)):
        if tab[x].location not in cities:
            cities.append(tab[x].location)
    return cities


def biggest_size_city(city, tab):
    size = tab[0].size
    for x in range(len(tab)):
        if city == tab[x].location:
            if tab[x].size > size:
                size = tab[x].size
    return size


def smallest_size_city(city, tab):
    size = tab[0].size
    for x in range(len(tab)):
        if city == tab[x].location:
            if tab[x].size < size:
                size = tab[x].size
    return size


def biggest_price_city(city, tab):
    price = tab[0].price
    for x in range(len(tab)):
        if city == tab[x].location:
            if tab[x].price > price:
                price = tab[x].price
    return price


def smallest_price_city(city, tab):
    price = tab[0].price
    for x in range(len(tab)):
        if city == tab[x].location:
            if tab[x].price < price:
                price = tab[x].price
    return price


def average_price_m2_city(city, tab):
    price = 0
    couter = 0
    for x in range(len(tab)):
        if city == tab[x].location:
            price = price + (tab[x].price / tab[x].size)
            couter = couter + 1
    return round(price / couter, 2)


def biggest_price_m2_city(city, tab):
    price = tab[0].price / tab[0].size
    for x in range(len(tab)):
        if city == tab[x].location:
            if tab[x].price / tab[x].size > price:
                price = tab[x].price
    return round(price, 2)


def smallest_price_m2_city(city, tab):
    price = tab[0].price / tab[0].size
    iter = 0
    for x in range(len(tab)):
        if city == tab[x].location:
            if tab[x].price / tab[x].size < price:
                price = tab[x].price / tab[x].size
                iter = x
    return round(price, 2)


def average_amount_rooms_city(city, tab):
    rooms = 0
    counter = 0
    for x in range(len(tab)):
        if city == tab[x].location:
            rooms = rooms + tab[x].rooms
            counter = counter + 1
    return round(rooms / counter, 2)


def average_amount_rooms(tab):
    rooms = 0
    for x in range(len(tab)):
        rooms = rooms + tab[x].rooms
    return round(rooms / len(tab), 2)


def most_frequent_city(tab):
    counter = 0
    num = tab[0]
    for i in tab:
        cur_freq = tab.count(i)
        if cur_freq > counter:
            counter = cur_freq
            num = i
    return num


def least_frequent_city(tab):
    return Counter(tab).most_common()[-1][0]


def amount_offer_city(city, tab):
    offers = 0
    for x in range(len(tab)):
        if city == tab[x].location:
            offers = offers + 1
    return offers


def average_size(tab):
    size = 0
    for x in range(len(tab)):
        size = size + tab[x].size
    return float(round(size / len(tab), 2))


def average_price(tab):
    price = 0
    for x in range(len(tab)):
        price = price + tab[x].price
    return float(round(price / len(tab), 2))


def most_expensive_flat(tab):
    price = 0
    nr = 0
    for x in range(len(tab)):
        if tab[x].price > price:
            price = tab[x].price
            nr = x
    return nr


def biggest_flat(tab):
    size = 0
    nr = 0
    for x in range(len(tab)):
        if tab[x].size > size:
            size = tab[x].size
            nr = x
    return nr
