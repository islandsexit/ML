import pandas as pd
import json
from geopy.geocoders import Nominatim
from datetime import date, datetime


def read():
    try:
        gibddid = input('Введите id происшествия, если есть')
        region = input('Введите region')
        parent_region = input('Введите parent region')
        date = datetime.today()
        address = input("Введите адресс")
        geolocator = Nominatim(user_agent="http")
        location = geolocator.geocode(address)
        df = pd.DataFrame([[gibddid, region, parent_region, date, address, location.latitude, location.longitude]],
                          columns=['gibddid', 'region', 'parent_region', 'date', 'address', 'lat', 'lon'])
        print(df)
    except:
        print('cheto')


if __name__ == '__main__':
    read()
