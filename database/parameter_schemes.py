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
    userId: int = None


class Userboard(BaseModel):
    id: int
    name_board: str


class Files(BaseModel):
    nameboard: str
    namefile: str
    contetn: str
    userId: int


class Userfile(BaseModel):
    id: int
    name_file: str
    content: str


class UserProfile(BaseModel):
    id: int
    user_name: str
