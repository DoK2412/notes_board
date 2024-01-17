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
    nameBoard: str  = Query(description='название доски')
    userId: int  = Query(default=None, description='id пользователя')


class Userboard(BaseModel):
    boardId: int
    nameBoard: str


class Card(BaseModel):
    boardId: int = Query(description='id  доски')
    nameCard: str = Query(description='название файла')
    userId: int = Query(description='id пользователя')


class UserCatd(BaseModel):
    cardId: int
    boardId: int
    nameCard: str


class UserCardOut(BaseModel):
    cardId: int
    boardId: int
    nameCard: str


class UserCardContent(BaseModel):
    listId: int
    namelist: str
    content: str


class UserProfile(BaseModel):
    id: int
    userName: str


class List(BaseModel):
    boardId: int = Query(description='id  доски')
    cardId: int = Query(description='id  карточки')
    nameList: str = Query(description='название файла')
    userId: int = Query(description='id пользователя')


class UserListdOut(BaseModel):
    listId: int
    nameList: str


class UserList(BaseModel):
    listId: int
    nameList: str


