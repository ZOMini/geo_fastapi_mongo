Проект работает:
http://130.193.37.228:9004/docs/

[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](http://130.193.37.228:9004/docs/)
[![Geo_API workflow](https://github.com/zomini/geo_fastapi_mongo/actions/workflows/main.yml/badge.svg)](https://github.com/zomini/zomini/geo_fastapi_mongo/actions/workflows/main.yml)

- sudo docker-compose exec web python script.py - при первом запуске(импорт данных, индексы БД).
- requests.http - тестовые запросы.


# MongoDB with FastAPI

This is a small sample project demonstrating how to build an API with [MongoDB](https://developer.mongodb.com/) and [FastAPI](https://fastapi.tiangolo.com/).
It was written to accompany a [blog post](https://developer.mongodb.com/quickstart/python-quickstart-fastapi/) - you should go read it!

## TL;DR

If you really don't want to read the [blog post](https://developer.mongodb.com/quickstart/python-quickstart-fastapi/) and want to get up and running,
activate your Python virtualenv, and then run the following from your terminal (edit the `DB_URL` first!):

```bash
# Install the requirements:
pip install -r requirements.txt

# Configure the location of your MongoDB database:
export MONGODB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"

# Start the service:
uvicorn app:app --reload
```

(Check out [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) if you need a MongoDB database.)

Now you can load http://localhost:8000/docs in your browser ... but there won't be much to see until you've inserted some data.

If you have any questions or suggestions, check out the [MongoDB Community Forums](https://developer.mongodb.com/community/forums/)!
