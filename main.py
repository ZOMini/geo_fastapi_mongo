from typing import List, Union

import motor.motor_asyncio
from fastapi import Body, FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response

from geo_api.models import GeoModel

MONGODB_URL="mongodb://localhost:27017/mongodb?retryWrites=true&w=majority"
 
app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.geo

@app.post("/",
          response_description="Add new geo",
          response_model=GeoModel)
async def create_geo(geo: GeoModel = Body(...)):
    geo = jsonable_encoder(geo)
    new_geo = await db["geo"].insert_one(geo)
    created_geo = await db["geo"].find_one({"_id": new_geo.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_geo)

@app.get("/",
         response_description="List all geo",
         response_model=List[GeoModel])
async def list_geo():
    geo = await db["geo"].find().to_list(1000)
    return geo


@app.get("/{id}/",
         response_description="Get a single geo",
         response_model=GeoModel)
async def show_geo(id: str):
    if (geo := await db["geo"].find_one({"_id": id})) is not None:
        return geo

    raise HTTPException(status_code=404, detail=f"Geo {id} not found")

@app.delete("/{id}", response_description="Delete a geo")
async def delete_geo(id: str):
    delete_result = await db["geo"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Geo {id} not found")
