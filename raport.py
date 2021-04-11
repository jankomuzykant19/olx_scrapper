import flat as f


def print_raport(flats):
    print(f'There were {len(flats)} offers parsed from OLX.')
    print(
        f'Flats were located among {len(f.get_all_cities(flats))} cities, the most offers were from {f.most_frequent_city(f.get_all_cities(flats))} ({f.amount_offer_city(f.most_frequent_city(f.get_all_cities(flats)), flats)}),'
        f' the least offers were from {f.least_frequent_city(f.get_all_cities(flats))} ({f.amount_offer_city(f.least_frequent_city(f.get_all_cities(flats)), flats)})')
    print(
        f'Average flat has {f.average_amount_rooms(flats)} rooms, size equal to {f.average_size(flats)} m2, costs {f.average_price(flats)} zł ({round((f.average_price(flats)/f.average_size(flats)),2)} zł/m2)')
    nr = f.most_expensive_flat(flats)
    nr2 = f.biggest_flat(flats)
    if nr == nr2:
        print(f'Most expensive and biggest offer - title: {flats[nr].name} || location: {flats[nr].location} || price: {flats[nr].price}zł || size: {flats[nr].size} m2 || amount of rooms: {flats[nr].rooms}\n')
    else:
        print(f'Most expensive offer - title: {flats[nr].name} || location: {flats[nr].location} || price: {flats[nr].price}zł || size: {flats[nr].size} m2 || amount of rooms: {flats[nr].rooms}')
        print(f'Biggest size of flat -  title: {flats[nr2].name} || location: {flats[nr2].location} || price: {flats[nr2].price}zł || size: {flats[nr2].size} m2 || amount of rooms: {flats[nr2].rooms}\n')
    cities = f.get_all_cities(flats)
    for x in range(len(cities)):
        print(f'City: {cities[x]}')
        print(f'Number of offers: {f.amount_offer_city(cities[x], flats)}')
        print(f'Average amount of rooms: {f.average_amount_rooms_city(cities[x], flats)}')
        print(
            f'Average price for m2: {f.average_price_m2_city(cities[x], flats)}zł/m2, biggest price for m2: {f.biggest_price_m2_city(cities[x], flats)}zł/m2, smallest price for m2: {f.smallest_price_m2_city(cities[x], flats)}zł/m2')
        print(
            f'Average price of flat: {f.average_price_city(cities[x], flats)}zł, biggest price of flat: {f.biggest_price_city(cities[x], flats)}zł, smallest price of flat: {f.smallest_price_city(cities[x], flats)}zł')
        print(
            f'Average size of flat: {f.average_size_city(cities[x], flats)} m2, biggest size of flat: {f.biggest_size_city(cities[x], flats)} m2, smallest size of flat: {f.smallest_size_city(cities[x], flats)} m2\n')
        break