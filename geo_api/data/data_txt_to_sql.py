import models
import pandas as pd
import var_geo
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017',
                     username='root',
                     password='mongopass')
db = client['geo']


def run():
    print('Импортируем данные! Займет 1 минуту. Ждем 354528 объекта.')
    df = pd.read_csv('geo_api/data/RU.txt',
                     delimiter='\t',
                     usecols=var_geo.COLUMNS,
                     na_values=None,
                     keep_default_na=False)
    df_dict: dict = df.to_dict('index')
    city_list = []
    suc = fau = 0
    for idx in df_dict.values():
        if idx['alternatenames'] is None:
            continue
        elif not var_geo.ALPHABET.isdisjoint(idx['alternatenames'].lower()):
            names = str(idx['alternatenames'])
            list_name = names.split(',')
            for i in list_name:
                if not var_geo.ALPHABET.isdisjoint(i.lower()):
                    idx['alternatenames'] = i
                    break
        else:
            idx['alternatenames'] = None
        try:
            city = models.GeoModel(
                geo_name_id=idx['geonameid'],
                name=idx['name'],
                ru_name=idx['alternatenames'],
                latitude=idx['latitude'],
                longitude=idx['longitude'],
                population=idx['population'],
                dem=idx['dem'],
                time_zone=idx['time zone'],
                mod_date=idx['modification date'],
            )
            city = jsonable_encoder(city)
            city_list.append(city)
            suc += 1
        except Exception:
            fau += 1
    print(db['geo'].count_documents({}))
    db["geo"].insert_many(city_list)
    print(db['geo'].count_documents({}))
    print('Закончили упражнение!')
    print(f'{suc} - успешно!')
    print(f'{fau} - неудачно!')


if __name__ == '__main__':
    run()
