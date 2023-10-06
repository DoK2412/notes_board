from database.connection_db import JobDb
import database.sql_requests as sql
from response_code import ResponseCode, ResponseCodeData

from database.parameter_schemes import Userboard


class Board:
    def __init__(self, user: int):
        self.user_id: int = user

    async def create_board(self, board_name: str):
        try:
            async with JobDb() as pool:
                board_user = await pool.fetchrow(sql.CHECK_BOARD, board_name, self.user_id)
                if board_user is None:
                    await pool.fetchrow(sql.NEW_BOARD, self.user_id, board_name)
                    return ResponseCode(1)
                else:
                    return ResponseCode(10)
        except Exception as exc:
            return ResponseCode(7)

    async def delete_board(self, board_name: str):
        try:
            async with JobDb() as pool:
                board_user = await pool.fetchrow(sql.CHECK_BOARD, board_name, self.user_id)
                if board_user:
                    await pool.fetchrow(sql.DETETE_BOARD, self.user_id, board_name)
                    await pool.fetch(sql.DETETE_BOARD_FILE, self.user_id, board_user['id'])
                    return ResponseCode(1)
                else:
                    return ResponseCode(9)
        except Exception as exc:
            return ResponseCode(7)

    async def get_board(self):
        try:
            last_doska = list()
            async with JobDb() as pool:
                boards = await pool.fetch(sql.GET_BOARD, self.user_id)
                if boards:
                    for i_board in boards:
                        board = Userboard(**i_board)
                        last_doska.append(board)
                    return ResponseCodeData(1, last_doska)
                else:
                    return ResponseCode(9)
        except Exception as exc:
            return ResponseCode(7)

    async def rename_board(self, board_old_name: str, board_new_name: str):
        try:
            async with JobDb() as pool:
                board_user = await pool.fetchrow(sql.CHECK_BOARD, board_old_name, self.user_id)
                if board_user:
                    await pool.fetchrow(sql.RENAME_BOLDER, board_new_name, self.user_id, board_old_name)
                    return ResponseCode(1)
                else:
                    return ResponseCode(9)
        except Exception as exc:
            return ResponseCode(7)
