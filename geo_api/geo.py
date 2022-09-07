from typing import Dict, List, Union

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from crud import db
from models import GeoModel
from sub_geo import RESP_200_SEARCH, RESP_200_TWO_CITES, delta_time, north_obj

geo_router = APIRouter(tags=['Main'])


@geo_router.get(
    '/geonameid/{geo_name_id}/',
    response_description='Get a single geo by GeoNameID',
    response_model=GeoModel,
    responses={404: {'description': 'Geo <geo_name_id> not found'}}
    )
async def show_geonameid(geo_name_id: int):
    if (
        geo := await db['geo'].find_one(
            {'geo_name_id': geo_name_id})) is not None:
        return geo
    raise HTTPException(status_code=404,
                        detail=f'Geo {geo_name_id} not found')


@geo_router.get(
    '/coordinates/',
    response_description='Get a single geo by GeoNameID',
    response_model=List[GeoModel],
    responses={404: {'description': 'Geo on this coordinates not found'}}
    )
async def geo_coor(lati_min: float,
                   lati_max: float,
                   longi_min: float,
                   longi_max: float,
                   cont: int):
    geo = (
        await db['geo']
        .find({'latitude': {'$lt': lati_max, '$gt': lati_min},
               'longitude': {'$lt': longi_max, '$gt': longi_min}})
        .to_list(cont))
    if len(geo) == 0:
        raise HTTPException(status_code=404,
                            detail='Geo on this coordinates not found')
    return geo


@geo_router.get(
    '/two_cites/',
    response_model=Union[List[GeoModel], List[Dict]],
    responses={404: {'description': 'Geo_1 or geo_2 not found'},
               200: RESP_200_TWO_CITES}
    )
async def two_cites(geo_1: str, geo_2: str):
    geo_1 = await (db['geo'].find({'ru_name': geo_1})
                            .sort('-population')
                            .to_list(1))
    geo_2 = await (db['geo'].find({'ru_name': geo_2})
                            .sort('population')
                            .to_list(1))
    if len(geo_1) == 0 or len(geo_2) == 0:
        raise HTTPException(status_code=404,
                            detail='geo_1 or geo_2 not found')
    north_object = north_obj(geo_1, geo_2)  # geo_api.sub_main
    tz, delta = delta_time(geo_1, geo_2)  # geo_api.sub_main
    extra = [{'northen object': north_object, 'equal time zone': tz + delta}]
    return JSONResponse(geo_1 + geo_2 + extra)


@geo_router.get(
    '/search/',
    response_model=List[GeoModel],
    responses={404: {'description': 'Geo_1 or geo_2 not found'},
               200: RESP_200_SEARCH}
    )
async def search(search: str):
    search = rf'\A{search}.*'
    geo = await db['geo'].find(
        {'ru_name': {'$regex': search, '$options': 's'}}).to_list(20)
    list_ru_name = []
    for ge in geo:
        list_ru_name.append(ge['ru_name'])
    list_ru_name = set(list_ru_name)
    return JSONResponse(list(list_ru_name))
