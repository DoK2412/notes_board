from fastapi import APIRouter, Request, Query, Response

from servise.user_login import authorization, registrations, get_profile
from servise.board import Board
from servise.file import File

from database.parameter_schemes import Usermadel, Boards, Files

from response_code import ResponseCode


servis_route = APIRouter()


@servis_route.get('/authentication', tags=['user_login'])
async def authentication(request: Request,
                         username: str = Query(None, description="Имя пользователя"),
                         password: str = Query(None, description="Пароль пользователя")):
    result = await authorization(request, username, password)
    return result


@servis_route.post('/registration', tags=['user_login'])
async def registration(request: Request,
                       user: Usermadel):
    result = await registrations(request, user.username, user.password, user.passwordConfig)
    return result


@servis_route.get('/logout', tags=['user_login'])
async def registration(request: Request):
    if request.session.get('userId'):
        request.session.clear()
        request.cookies.clear()
        return ResponseCode(1)
    else:
        return ResponseCode(2)

@servis_route.get('/profile', tags=['user_login'])
async def profile(request: Request,
                  userId: int = Query(None, description="Id пользователя")):
    if userId is not None:
        result = await get_profile(request, userId)
        return result
    else:
        return ResponseCode(2)


@servis_route.post('/createBoard', tags=['board'])
async def create_board(request: Request,
                       board: Boards):
    if board.userId is not None:
        result = await Board(board.userId).create_board(board.nameboard)
        return result
    else:
        return ResponseCode(2)


@servis_route.delete('/deleteBoard', tags=['board'])
async def delete_board(request: Request,
                       nameBolder: str = Query(description="Название рабочего пространства"),
                       userId: int = Query(None, description="Id пользователя")):
    if userId is not None:
        result = await Board(userId).delete_board(nameBolder)
        return result
    else:
        return ResponseCode(2)


@servis_route.get('/getBoard', tags=['board'])
async def get_board(request: Request,
                    userId: int = Query(None, description="Id пользователя")):
    if userId is not None:
        result = await Board(userId).get_board()
        return result
    else:
        return ResponseCode(2)


@servis_route.put('/renameBoard', tags=['board'])
async def get_board(request: Request,
                    boardOldName: str = Query(description="Старое название рабочего пространства"),
                    boardNewName: str = Query(description="Новое название рабочего пространства"),
                    userId: int = Query(None, description="Id пользователя")):
    if userId is not None:
        result = await Board(userId).rename_board(boardOldName, boardNewName)
        return result
    else:
        return ResponseCode(2)


@servis_route.post('/createFile', tags=['file'])
async def create_file(request: Request,
                       file: Files):
    if file.userId is not None:
        result = await File(file.nameboard, file.userId).create_file(file.namefile, file.contetn)
        return result
    else:
        return ResponseCode(2)


@servis_route.get('/getFile', tags=['file'])
async def get_file(request: Request,
                   boardName: str = Query(description="Название рабочего пространства"),
                   userId: int = Query(None, description="Id пользователя")):
    if userId is not None:
        result = await File(boardName, userId).get_file()
        return result
    else:
        return ResponseCode(2)


@servis_route.delete('/deleteFile', tags=['file'])
async def delete_file(request: Request,
                      fileName: str = Query(description="Название файла для удаления"),
                      boardName: str = Query(description="Название файла для удаления"),
                      userId: int = Query(None, description="Id пользователя")):
    if userId is not None:
        result = await File(boardName, userId).delete_file(fileName)
        return result
    else:
        return ResponseCode(2)


@servis_route.put('/renameFile', tags=['file'])
async def rename_file(request: Request,
                      fileOldName: str = Query(description="Старое название файла"),
                      fileNewName: str = Query(description="Новое название файла"),
                      boardName: str = Query(description="Название файла для удаления"),
                      userId: int = Query(None, description="Id пользователя")):
    if userId is not None:
        result = await File(boardName, userId).rename_file(fileOldName, fileNewName)
        return result
    else:
        return ResponseCode(2)


@servis_route.put('/updateFile', tags=['file'])
async def rename_file(request: Request,
                      nameFile: str = Query(description="Название файла"),
                      contetn: str = Query(description="Обновленные данные в файле"),
                      boardName: str = Query(description="Название файла для удаления"),
                      userId: int = Query(None, description="Id пользователя")):
    if userId is not None:
        result = await File(boardName, userId).update_file(nameFile, contetn)
        return result
    else:
        return ResponseCode(2)
