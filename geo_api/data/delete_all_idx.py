from pymongo import MongoClient

client = MongoClient('mongodb://root:mongopass@mongo')
# client = MongoClient('mongodb://127.0.0.1:27017',
#                      username='root',
#                      password='mongopass')
db = client['geo']
geo_db = db['geo']

print('Были индексы:')
print(sorted(list(geo_db.index_information())))
geo_db.drop_indexes()
print('Текущие индексы:')
print(sorted(list(geo_db.index_information())))
