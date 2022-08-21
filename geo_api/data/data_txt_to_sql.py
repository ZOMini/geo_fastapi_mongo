import pandas as pd
import var_geo
from models import GeoObj
from redis_om import Migrator


def run():
    print('Импортируем данные! Займет 1 минуту. Ждем 354528 объекта.')
    df = pd.read_csv('./data/test.txt',
                    delimiter='\t',
                    usecols=var_geo.COLUMNS,
                    na_values=None,
                    keep_default_na=False)
    df_dict:dict = df.to_dict('index')
    suc = fau = 0
    Migrator().run()
    city = GeoObj(
                geo_name_id = 111111111,
                name = "sadasdasd",
                ru_name = "sdasdasdasd",
                latitude = 15.1,
                longitude = 16.1,
                population = 11111,
                dem = 222222,
                time_zone = 'qweqwtret',
                mod_date = '2009-08-07'
            )
    # for idx in df_dict.values():
    #     if idx['alternatenames'] == None: continue
    #     elif not var_geo.ALPHABET.isdisjoint(idx['alternatenames'].lower()):
    #         names = str(idx['alternatenames'])
    #         list_name = names.split(',')
    #         for i in list_name:
    #             if not var_geo.ALPHABET.isdisjoint(i.lower()):
    #                 idx['alternatenames'] = i
    #                 break
    #     else:
    #         idx['alternatenames'] = None
    #     try:
    #         city = GeoObj(
    #             geo_name_id = idx['geonameid'],
    #             name = idx['name'],
    #             ru_name = idx['alternatenames'],
    #             latitude = idx['latitude'],
    #             longitude = idx['longitude'],
    #             population = idx['population'],
    #             dem = idx['dem'],
    #             time_zone = idx['time zone'],
    #             mod_date = idx['modification date'],
    #         )
    #         city.save()
    #         # list_city.append(city)
    #         suc += 1
    #     except Exception as e: 
    #         fau += 1
    print(city.pk)
    city.save()
    print('Закончили упражнение!')
    print(f'{suc} - успешно!')
    print(f'{fau} - неудачно!')

if __name__ == '__main__':
    run()
