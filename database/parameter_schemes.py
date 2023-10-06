from pydantic import BaseModel

from fastapi import Query


class DataBase(BaseModel):
    """
    Конфигурация Базы Данных
    """
    user: str
    password: str
    db_name: str
    host: str
    port: int


class Config(BaseModel):
    DataBase: DataBase


class Authorization(BaseModel):
    mail: str = Query(description='Почта пользователя')


class Usermadel(BaseModel):
    username: str
    password: str
    passwordConfig: str


class Boards(BaseModel):
    nameboard: str


class Userboard(BaseModel):
    id: int
    name_doska: str
