import matplotlib.pyplot as plt
import numpy as np

import flat as f


def get_avg_city_size(flats):
    avg_city_size = []
    for x in range(len(f.get_all_cities(flats))):
        avg_city_size.append(f.average_size_city(f.get_all_cities(flats)[x], flats))
    return avg_city_size


def get_avg_city_price(flats):
    avg_city_price = []
    for x in range(len(f.get_all_cities(flats))):
        avg_city_price.append(f.average_price_city(f.get_all_cities(flats)[x], flats))
    return avg_city_price


def get_avg_city_price_m2(flats):
    avg_city_price_m2 = []
    for x in range(len(f.get_all_cities(flats))):
        avg_city_price_m2.append(f.average_price_m2_city(f.get_all_cities(flats)[x], flats))
    return avg_city_price_m2


def city_size(cities, sizes):
    height = sizes
    bars = cities
    y_pos = np.arange(len(height))
    plt.figure(figsize=(17, 10))
    plt.barh(y_pos, height, color='#969696')
    plt.yticks(y_pos, bars)
    plt.xlabel('Average size of flat', fontsize=12, color='#323232')
    plt.ylabel('City', fontsize=12, color='#323232')
    plt.title('Lodzkie Voivodship 2021', fontsize=16, color='#323232')
    plt.show()


def city_price(cities, prices):
    height = prices
    bars = cities
    y_pos = np.arange(len(height))
    plt.figure(figsize=(17, 10))
    plt.barh(y_pos, height, color='#969696')
    plt.yticks(y_pos, bars)
    plt.xlabel('Average price of flat', fontsize=12, color='#323232')
    plt.ylabel('City', fontsize=12, color='#323232')
    plt.title('Lodzkie Voivodship 2021', fontsize=16, color='#323232')
    plt.show()


def city_price_m2(cities, prices):
    height = prices
    bars = cities
    y_pos = np.arange(len(height))
    plt.figure(figsize=(17, 10))
    plt.barh(y_pos, height, color='#969696')
    plt.yticks(y_pos, bars)
    plt.xlabel('Average price of m2', fontsize=12, color='#323232')
    plt.ylabel('City', fontsize=12, color='#323232')
    plt.title('Lodzkie Voivodship 2021', fontsize=16, color='#323232')
    plt.show()
