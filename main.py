# https://miroslawmamczur.pl/002-wykres-kolumnowy-bar-plot/
# TODO:
# Pomyśleć nad wprowadzaniem danych przez użytkownika
# Więcej wykresów
# Testy dla innych województw
import flat as f
import parse as p
import plot as pl
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

pl.city_size(f.get_all_cities(flats), pl.get_avg_city_size(flats))
pl.city_price(f.get_all_cities(flats), pl.get_avg_city_price(flats))
pl.city_price_m2(f.get_all_cities(flats), pl.get_avg_city_price_m2(flats))
