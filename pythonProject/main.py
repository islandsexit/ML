import pandas as pd
import json
from geopy.geocoders import Nominatim
from datetime import datetime
import geocoder

def read():

        g = geocoder.location(input('Где это произошло?'))
        print("Вы знаете точные координаты")
        answer = input()
        if answer == "Да":
                ...
        print("Это сегодня произошло? ")
        answer = input()
        if answer == "Да":
            date = datetime.today()
        else:
            date = datetime.strptime(input("Введи дату в формате 18.08.21 18:00"), '%d.%m.%y %H:%M')
        gibddid = input('Введите id происшествия, если есть '  )
        region = input('Введите region ')
        parent_region = input('Введите parent region ')

        feat = input("Опишите ДТП (Что находилось рядом, освещение, состояние дороги)")
        inj = input('Сколько пострадавших? Ответ в числовом формате')
        dead = input('Сколько человек погибло? Ответ в числовом формате')

        df = pd.DataFrame([[gibddid, region, parent_region, date, g.location, g.latitudeg.latitude, g.longitudeg.longitude, feat, inj,dead]],
                          columns=['gibddid', 'region', 'parent_region', 'date', 'address', 'lat', 'lon', 'feat', 'inj_count', 'dead_count'])
        print(df)



if __name__ == '__main__':
    read()
