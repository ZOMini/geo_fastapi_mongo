from tkinter.tix import TEXT

from pymongo import ASCENDING, TEXT, MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['geo']
geo_db = db['geo']

print('Были индексы:')
print(sorted(list(geo_db.index_information())))
geo_db.create_index([('ru_name', TEXT)])
geo_db.create_index([('ru_name', ASCENDING)])
geo_db.create_index([('geo_name_id', ASCENDING)], unique=True)
print('Текущие индексы:')
print(sorted(list(geo_db.index_information())))
