from typing import Dict, List, Union

import motor.motor_asyncio
import uvicorn
from fastapi import Body, FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response

from geo_api.models import GeoModel
from geo_api.sub_main import delta_time, north_obj

MONGODB_URL="mongodb://localhost:27017/mongodb?retryWrites=true&w=majority"
 
app = FastAPI(debug=True)
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.geo

@app.post("/test/",
          response_description="Add new geo",
          response_model=GeoModel)
async def create_geo(geo: GeoModel = Body(...)):
    geo = jsonable_encoder(geo)
    new_geo = await db["geo"].insert_one(geo)
    created_geo = await db["geo"].find_one({"_id": new_geo.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_geo)

@app.get("/test/",
         response_description="List all geo",
         response_model=List[GeoModel])
async def list_geo():
    geo = await db["geo"].find().to_list(100)
    return geo


@app.get("/test/{id}/",
         response_description="Get a single geo",
         response_model=GeoModel)
async def show_geo(id: str):
    if (geo := await db["geo"].find_one({"_id": id})) is not None:
        return geo

    raise HTTPException(status_code=404, detail=f"Geo {id} not found")

@app.delete("/test/{id}", response_description="Delete a geo")
async def delete_geo(id: str):
    delete_result = await db["geo"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Geo {id} not found")

@app.get("/geonameid/{geo_name_id}/",
         response_description="Get a single geo by GeoNameID",
         response_model=GeoModel)
async def show_geonameid(geo_name_id: int):
    if (geo := await db["geo"].find_one({"geo_name_id": geo_name_id})) is not None:
        return geo
    raise HTTPException(status_code=404, detail=f"Geo {geo_name_id} not found")

@app.get("/coordinates/",
         response_description="Get a single geo by GeoNameID",
         response_model=List[GeoModel],
         responses={404: {'detail': 'Not Found'}})
async def geo_coor(lati_min: float,
                   lati_max: float,
                   longi_min: float,
                   longi_max: float,
                   cont:int):
    geo = (await db["geo"]
        .find({"latitude":{"$lt":lati_max,"$gt":lati_min},
               "longitude":{"$lt":longi_max,"$gt":longi_min}})
        .to_list(cont))
    if len(geo) == 0:
        raise HTTPException(status_code=404, detail=f"Geo on this coordinate not found")
    return geo

@app.get("/two_cites/",
         response_description="Two geo object + northen object + equal time zone",
         response_model=Union[List[GeoModel], List[Dict]],
         responses={404: {'detail': 'Not Found'}})
async def two_cites(geo_1: str, geo_2: str):
    geo_1 = await db["geo"].find({"ru_name": geo_1}).sort("-population").to_list(1)
    geo_2 = await db["geo"].find({"ru_name": geo_2}).sort("population").to_list(1)
    if len(geo_1) == 0 or len(geo_2) == 0:
        raise HTTPException(status_code=404, detail=f"geo_1 or geo_2 is empty")
    north_object = north_obj(geo_1, geo_2) # geo_api.sub_main
    tz, delta = delta_time(geo_1, geo_2) # geo_api.sub_main
    extra = [{"northen object": north_object, "equal time zone": tz + delta}]
    return JSONResponse(geo_1 + geo_2 + extra)

@app.get("/search/",
         response_description="List search ru name geo",
         response_model=List)
async def search(search: str):
    search = "\A" + search + ".*"
    # geo = await db["geo"].find({"$text": {"$search": search, "$language": "ru"}}).to_list(10)
    # geo = await db["geo"].find({"$or": [{"$text": {"$search": search, "$language": "ru"}}, {"ru_name": {"$regex": search}}]}).to_list(10)
    geo = await db["geo"].find({"ru_name": {"$regex": search}}).to_list(20)
    list_ru_name = []
    for ge in geo:
        list_ru_name.append(ge['ru_name'])
    list_ru_name = set(list_ru_name)
    return list_ru_name


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
