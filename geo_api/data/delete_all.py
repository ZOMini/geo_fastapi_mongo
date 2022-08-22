from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['geo']
geo_db = db['geo']


def run():
    print(geo_db.count_documents({}))
    geo_db.delete_many({})
    print(geo_db.count_documents({}))


if __name__ == '__main__':
    run()
