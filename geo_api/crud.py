from typing import List

import motor.motor_asyncio as moto
from fastapi import APIRouter, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response

from models import GeoModel, GeoModelUpd

MONGODB_URL = 'mongodb://localhost:27017/mongodb?retryWrites=true&w=majority'

client = moto.AsyncIOMotorClient(MONGODB_URL)
db = client.geo

crud_router = APIRouter(prefix='/crud', tags=['Base CRUD'])


@crud_router.post('/',
                  response_description='Add new geo',
                  response_model=GeoModel)
async def create_geo(geo: GeoModel = Body(...)):
    geo = jsonable_encoder(geo)
    new_geo = await db['geo'].insert_one(geo)
    created_geo = await db['geo'].find_one({'_id': new_geo.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED,
                        content=created_geo) 


@crud_router.get('/',
                 response_description='List all geo',
                 response_model=List[GeoModel])
async def list_geo():
    geo = await db['geo'].find().to_list(100)
    return geo


@crud_router.get('/{id}/',
                 response_description='Get a single geo',
                 response_model=GeoModel)
async def show_geo(id: str):
    if (geo := await db['geo'].find_one({'_id': id})) is not None:
        return geo

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Geo {id} not found')


@crud_router.put('/{id}',
                 response_description='Update a Geo',
                 response_model=GeoModelUpd)
async def update_geo(id: str, geo: GeoModelUpd = Body(...)):
    geo = {k: v for k, v in geo.dict().items() if v is not None}

    if len(geo) >= 1:
        update_result = await db['geo'].update_one({'_id': id}, {'$set': geo})

        if update_result.modified_count == 1:
            if (
                updated_geo := await db['geo'].find_one({'_id': id})
            ) is not None:
                return updated_geo

    if (existing_geo := await db['geo'].find_one({'_id': id})) is not None:
        return existing_geo


@crud_router.delete('/{id}', response_description='Delete a geo')
async def delete_geo(id: str):
    delete_result = await db['geo'].delete_one({'_id': id})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f'Geo {id} not found')
