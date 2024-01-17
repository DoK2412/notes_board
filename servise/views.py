from fastapi import APIRouter, Request, Query, Response

from servise.user_login import authorization, registrations, get_profile
from servise.board import Board
from servise.card import File
from servise.list import Lists

from database.parameter_schemes import Usermadel, Boards, Card, List

from response_code import ResponseCode


servis_route = APIRouter()


@servis_route.get('/authentication', tags=['user_login'])
async def authentication(request: Request,
                         username: str = Query(None, description="Имя пользователя"),
                         password: str = Query(None, description="Пароль пользователя")):
    '''Авторизация пользователя в системе'''
    result = await authorization(request, username, password)
    return result


@servis_route.post('/registration', tags=['user_login'])
async def registration(request: Request,
                       user: Usermadel):
    '''Регистрация пользователя в системе'''
    result = await registrations(request, user.username, user.password, user.passwordConfig)
    return result


@servis_route.get('/logout', tags=['user_login'])
async def registration(request: Request):
    '''Не используется'''
    if request.session.get('userId'):
        request.session.clear()
        request.cookies.clear()
        return ResponseCode(1)
    else:
        return ResponseCode(2)

@servis_route.get('/profile', tags=['user_login'])
async def profile(request: Request,
                  userId: int = Query(None, description="Id пользователя")):
    '''Получение профиля пользователя'''
    if userId is not None:
        result = await get_profile(request, userId)
        return result
    else:
        return ResponseCode(2)


@servis_route.post('/createBoard', tags=['board'])
async def create_board(request: Request,
                       board: Boards):
    '''Создание доски пользователя'''
    if board.userId is not None:
        result = await Board(board.userId).create_board(board.nameBoard)
        return result
    else:
        return ResponseCode(2)


@servis_route.delete('/deleteBoard', tags=['board'])
async def delete_board(request: Request,
                       boardId: int = Query(description="id рабочего пространства"),
                       userId: int = Query(None, description="Id пользователя")):
    '''Удаление доски пользователя'''
    if userId is not None:
        result = await Board(userId).delete_board(boardId)
        return result
    else:
        return ResponseCode(2)


@servis_route.get('/getBoard', tags=['board'])
async def get_board(request: Request,
                    userId: int = Query(None, description="Id пользователя")):
    '''Получение ебщего количества досок у пользователя'''
    if userId is not None:
        result = await Board(userId).get_board()
        return result
    else:
        return ResponseCode(2)


@servis_route.put('/renameBoard', tags=['board'])
async def get_board(request: Request,
                    boardId: int = Query(description="id рабочего пространства"),
                    boardNewName: str = Query(description="Новое название рабочего пространства"),
                    userId: int = Query(None, description="Id пользователя")):
    '''Переименование доски пользователя'''
    if userId is not None:
        result = await Board(userId).rename_board(boardId, boardNewName)
        return result
    else:
        return ResponseCode(2)


@servis_route.post('/createСard', tags=['card'])
async def create_file(request: Request,
                       card: Card):
    '''Создание контента в доске пользователя (то что будет находится внутри доски)'''
    print(card)
    if card.userId is not None:
        result = await File(card.boardId, card.userId).create_card(card.nameCard)
        return result
    else:
        return ResponseCode(2)


@servis_route.get('/getCard', tags=['card'])
async def get_file(request: Request,
                   boardId: int = Query(description="Id рабочего пространства"),
                   userId: int = Query(None, description="Id пользователя")):
    '''Получить все содержимое контента в определенной доске'''
    if userId is not None:
        result = await File(boardId, userId).get_card()
        return result
    else:
        return ResponseCode(2)


@servis_route.delete('/deleteCard', tags=['card'])
async def delete_file(request: Request,
                      cardId: int = Query(description="Id файла для удаления"),
                      boarId: int = Query(description="Id доски"),
                      userId: int = Query(None, description="Id пользователя")):
    '''Удаление контента из определенной доски'''
    if userId is not None:
        result = await File(boarId, userId).delete_file(cardId)
        return result
    else:
        return ResponseCode(2)


@servis_route.put('/renameCard', tags=['card'])
async def rename_file(request: Request,
                      cardId: int = Query(description="Id файла"),
                      cardNewName: str = Query(description="Новое название файла"),
                      boardId: int = Query(description="Id доски"),
                      userId: int = Query(None, description="Id пользователя")):
    '''Переименование контента находящегося в определенной доске'''
    if userId is not None:
        result = await File(boardId, userId).rename_card(cardId, cardNewName)
        return result
    else:
        return ResponseCode(2)


@servis_route.post('/createList', tags=['list'])
async def create_card(request: Request,
                       list: List):
    '''Создание контента в доске пользователя (то что будет находится внутри доски)'''
    if list.userId is not None:
        result = await Lists(list.boardId, list.userId, list.cardId).create_list(list.nameList)
        return result
    else:
        return ResponseCode(2)


@servis_route.get('/getList', tags=['list'])
async def get_file(request: Request,
                   cardId: int = Query(description="Id файла"),
                   boardId: int = Query(description="Id рабочего пространства"),
                   userId: int = Query(None, description="Id пользователя")):
    '''Получить все содержимое контента в определенной доске'''
    if userId is not None:
        result = await Lists(boardId, userId, cardId).get_list()
        return result
    else:
        return ResponseCode(2)

@servis_route.get('/deleteList', tags=['list'])
async def get_file(request: Request,
                   listId: int = Query(description="Id списка"),
                   cardId: int = Query(description="Id файла"),
                   boardId: int = Query(description="Id рабочего пространства"),
                   userId: int = Query(None, description="Id пользователя")):
    '''Получить все содержимое контента в определенной доске'''
    if userId is not None:
        result = await Lists(boardId, userId, cardId).delete_list(listId)
        return result
    else:
        return ResponseCode(2)


@servis_route.put('/renameList', tags=['list'])
async def rename_file(request: Request,
                      listId: int = Query(description="Id списка"),
                      listNewName: str = Query(description="Новое название файла"),
                      cardId: int = Query(description="Id карточки"),
                      boardId: int = Query(description="Id доски"),
                      userId: int = Query(None, description="Id пользователя")):
    '''Переименование контента находящегося в определенной доске'''
    if userId is not None:
        result = await Lists(boardId, userId, cardId).rename_list(listId, listNewName)
        return result
    else:
        return ResponseCode(2)


@servis_route.put('/addContentList', tags=['card'])
async def rename_card(request: Request,
                      listId: int = Query(description="Id списка"),
                      cardId: int = Query(description="Id файла"),
                      content: str = Query(description="данные в файле"),
                      boardId: int = Query(description="Id доски"),
                      userId: int = Query(None, description="Id пользователя")):
    '''Обновить содержимое определенного контента в доске'''
    if userId is not None:
        result = await Lists(boardId, userId, cardId).add_list_content(listId, content)
        return result
    else:
        return ResponseCode(2)


@servis_route.get('/getContentList', tags=['card'])
async def rename_card(request: Request,
                      listId: int = Query(description="Id списка"),
                      cardId: int = Query(description="Id файла"),
                      boardId: int = Query(description="Id доски"),
                      userId: int = Query(None, description="Id пользователя")):
    '''Обновить содержимое определенного контента в доске'''
    if userId is not None:
        result = await Lists(boardId, userId, cardId).get_list_content(listId)
        return result
    else:
        return ResponseCode(2)