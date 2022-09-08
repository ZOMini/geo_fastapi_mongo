import uvicorn

"""При работе Motor(motor_asyncio) + uvicorn нужно запускать отдельным файлом.
   Недооптимизировано). (https://github.com/tiangolo/fastapi/issues/3854) """
if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8004, reload=True)
