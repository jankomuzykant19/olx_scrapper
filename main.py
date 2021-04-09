# https://miroslawmamczur.pl/002-wykres-kolumnowy-bar-plot/
# TODO:
# Pomyśleć nad wprowadzaniem danych przez użytkownika
# Więcej wykresów
# Testy dla innych województw
import parse as p
import raport as r

choice = input("[1] Scrape offers from OLX\n[2] Get offers from database\n")
if choice == "1":
    p.delete_offers()
    for page in range(1, 26):
        p.parse_page(page)
    flats = p.get_data_from_db()

if choice == "2":
    flats = p.get_data_from_db()

r.print_raport(flats)

avg_city_size = []
avg_city_price = []
avg_city_price_m2 = []
#for x in range(len(f.get_all_cities(flats))):
#     avg_city_size.append(f.average_size_city(f.get_all_cities(flats)[x], flats))
#     avg_city_price.append(f.average_price_city(f.get_all_cities(flats)[x], flats))
#     avg_city_price_m2.append(f.average_price_m2_city(f.get_all_cities(flats)[x], flats))

# plot.city_size(f.get_all_cities(flats), avg_city_size)
# plot.city_price(f.get_all_cities(flats), avg_city_price)
# plot.city_price_m2(f.get_all_cities(flats), avg_city_price_m2)

