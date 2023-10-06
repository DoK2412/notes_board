from fastapi import APIRouter, Request, Query

from servise.user_login import authorization, registrations
from servise.board import Board

from database.parameter_schemes import Usermadel, Boards

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
    if request.session.get('user_id'):
        request.session.clear()
        return ResponseCode(1)
    else:
        return ResponseCode(2)


@servis_route.post('/createBoard', tags=['board'])
async def create_board(request: Request,
                       board: Boards):
    if request.session.get('user_id'):
        result = await Board(request.session['user_id']).create_board(board.nameboard)
        return result
    else:
        return ResponseCode(2)


@servis_route.delete('/deleteBoard', tags=['board'])
async def delete_board(request: Request,
                       name_bolder: str = Query(description="Название рабочего пространства")):
    if request.session.get('user_id'):
        result = await Board(request.session['user_id']).delete_board(name_bolder)
        return result
    else:
        return ResponseCode(2)


@servis_route.get('/getBoard', tags=['board'])
async def get_board(request: Request):
    if request.session.get('user_id'):
        result = await Board(request.session['user_id']).get_board()
        return result
    else:
        return ResponseCode(2)


@servis_route.get('/renameBoard', tags=['board'])
async def get_board(request: Request,
                    board_old_name: str = Query(description="Старое название рабочего пространства"),
                    board_new_name: str = Query(description="Новое название рабочего пространства")):
    if request.session.get('user_id'):
        result = await Board(request.session['user_id']).rename_board(board_old_name, board_new_name)
        return result
    else:
        return ResponseCode(2)
