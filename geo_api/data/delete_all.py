from crud import MONGODB_URL
from pymongo import MongoClient

client = MongoClient(MONGODB_URL)
# client = MongoClient('mongodb://127.0.0.1:27017',
#                      username='root',
#                      password='mongopass')
db = client['geo']
geo_db = db['geo']


def run():
    print(geo_db.count_documents({}))
    geo_db.delete_many({})
    print(geo_db.count_documents({}))


if __name__ == '__main__':
    run()
