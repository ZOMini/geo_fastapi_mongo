FROM python:3.9.7-slim
WORKDIR /geo_api
COPY geo_api/ .
RUN pip install -r requirements.txt
CMD ["python3", "uvicorn_run.py"] 
