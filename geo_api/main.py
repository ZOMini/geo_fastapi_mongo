from fastapi import FastAPI

from crud import crud_router
from geo import geo_router

app = FastAPI(debug=True)
app.include_router(crud_router, prefix='/api/v1')
app.include_router(geo_router, prefix='/api/v1')
