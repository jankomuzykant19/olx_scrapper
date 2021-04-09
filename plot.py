import matplotlib.pyplot as plt
import numpy as np


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
