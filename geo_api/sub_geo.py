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
