from typing import Union

from bson import ObjectId
from pydantic import BaseModel, Field


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


class GeoModelUpd(BaseModel):
    geo_name_id: int = Field(...)
    name: str = Field(...)
    ru_name: Union[str, None] = Field(...)
    latitude: float = Field(gt=-90.0,
                            lt=90.0,
                            title='Широта',
                            description='от -90 до +90')
    longitude: float = Field(gt=-180.0,
                             lt=180.0,
                             title='Долгота',
                             description='от -180 до +180')
    population: Union[int, None] = Field(gt=-1,
                                         title='Население',
                                         description='больше 0')
    dem: Union[int, None] = Field(gt=-1,
                                  title='Площадь в м',
                                  description='больше 0')
    time_zone: Union[str, None] = Field(title='Таймзона',
                                        description='datetime.tzinfo')
    mod_date: Union[str, None] = Field(title='Дата модификации',
                                       description='ГГГГ-ММ-ДД')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example': {
                'geo_name_id': 12492934,
                'name': 'Klostova',
                'ru_name': 'Клостова',
                'latitude': 55.63086,
                'longitude': 37.1881100,
                'population': 100000,
                'dem': 192,
                'time_zone': 'Europe/Moscow',
                'mod_date': '2022-08-04'
            }
        }


class GeoModel(GeoModelUpd):

    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            'example': {
                '_id': '6302075722b087cddd6876b0',
                'geo_name_id': 12492934,
                'name': 'Klostova',
                'ru_name': 'Клостова',
                'latitude': 55.63086,
                'longitude': 37.1881100,
                'population': 100000,
                'dem': 192,
                'time_zone': 'Europe/Moscow',
                'mod_date': '2022-08-04'
            }
        }
