import pytz

COLUMNS = ['geonameid',
           'name',
           'alternatenames',
           'latitude',
           'longitude',
           'population',
           'dem',
           'time zone',
           'modification date']
ALPHABET = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
