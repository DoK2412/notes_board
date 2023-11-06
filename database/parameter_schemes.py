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
    nameBoard: str
    userId: int = None


class Userboard(BaseModel):
    id: int
    nameBoard: str


class Files(BaseModel):
    nameBoard: str
    nameFile: str
    contetn: str
    userId: int


class Userfile(BaseModel):
    id: int
    nameFile: str
    content: str


class UserProfile(BaseModel):
    id: int
    userName: str
