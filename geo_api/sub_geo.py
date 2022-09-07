def north_obj(geo_1, geo_2):
    if geo_1[0]['latitude'] > geo_2[0]['latitude']:
        north_object = geo_1[0]['ru_name']
    else:
        north_object = geo_2[0]['ru_name']
    north_object += ' - находится севернее!'
    return north_object


def delta_time(city_1, city_2):
    from datetime import datetime as dt

    import pytz

    if city_1[0]['time_zone'] == city_2[0]['time_zone']:
        t_z = 'Временные зоны одинаковые.'
        delta_time = ''
    else:
        t_z = 'Временные зоны разные - '
        dtObject_1 = dt.now(pytz.timezone(city_1[0]['time_zone']))
        dtObject_2 = dt.now(pytz.timezone(city_2[0]['time_zone']))
        dt_delta = abs((int(dt.strftime(dtObject_2, '%z'))
                        - int(dt.strftime(dtObject_1, '%z'))) // 100)
        if dtObject_1 > dtObject_2:
            c_1 = city_1[0]['ru_name']
            delta_time = f'В городе {c_1} время на {dt_delta} часов больше.'
        else:
            c_2 = city_2[0]['ru_name']
            delta_time = f'В городе {c_2} время на {dt_delta} часов больше.'
    return t_z, delta_time

# For schemas


RESPONSE_200_TWO_CITES_LIST = [
  {
    "_id": "630366c88678a04d58b4a363",
    "geo_name_id": 12459893,
    "name": "Gora Zaslonka",
    "ru_name": "Гора Заслонка",
    "latitude": 52.5994,
    "longitude": 105.75356,
    "population": 0,
    "dem": 788,
    "time_zone": "Asia/Irkutsk",
    "mod_date": "2022-04-20"
  },
  {
    "_id": "630366b78678a04d58b0cd30",
    "geo_name_id": 575154,
    "name": "Bol’shaya Derevnya",
    "ru_name": "Большая",
    "latitude": 59.58911,
    "longitude": 40.92052,
    "population": 0,
    "dem": 129,
    "time_zone": "Europe/Moscow",
    "mod_date": "2012-01-17"
  },
  {
    "northen object": "Большая - находится севернее!",
    "equal time zone":
    "Временные зоны разные - В городе Большая время на 5 часов больше."
  }
]

RESP_200_TWO_CITES = {
            "description": "Two geo object + northen object + equal time zone",
            "content": {
                "application/json": {
                    "example": RESPONSE_200_TWO_CITES_LIST
                }
            },
        }

RESP_200_SEARCH_LIST = [
  "Василева",
  "Василево",
  "Василев Майдан",
  "Василек",
  "Васили",
  "Василеостровский",
  "Василисино",
  "Василевичи",
  "Василеостровский район",
  "Василисина",
  "Василовка",
  "Василисово"
]

RESP_200_SEARCH = {
            "description": "List search ru name geo",
            "content": {
                "application/json": {
                    "example": RESP_200_SEARCH_LIST
                }
            },
        }
