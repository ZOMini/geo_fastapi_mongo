from crud import MONGODB_URL
from pymongo import ASCENDING, TEXT, MongoClient

client = MongoClient(MONGODB_URL)
# client = MongoClient('mongodb://127.0.0.1:27017',
#                      username='root',
#                      password='mongopass')
db = client['geo']
geo_db = db['geo']

print('Были индексы:')
print(sorted(list(geo_db.index_information())))
geo_db.create_index([('ru_name', TEXT)])
geo_db.create_index([('ru_name', ASCENDING)])
geo_db.create_index([('geo_name_id', ASCENDING)])
print('Текущие индексы:')
print(sorted(list(geo_db.index_information())))
