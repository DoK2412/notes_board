from database.connection_db import JobDb

from database.parameter_schemes import Userfile

import database.sql_requests as sql
from response_code import ResponseCode, ResponseCodeData


class File:
    def __init__(self, boald: str, user: int):
        self.user_id: int = user
        self.boald: str = boald

    async def create_file(self, file_name: str, contetn: str):
        async with JobDb() as pool:
            board_id = await pool.fetchrow(sql.CHECK_BOARD, self.boald, self.user_id)
            if board_id:
                check_file = await pool.fetchrow(sql.CHECK_FILE, file_name, self.user_id)
                if check_file is None:
                    await pool.fetchrow(sql.NEW_FILE, self.user_id, board_id['id'], file_name, contetn)
                    return ResponseCode(1)
                else:
                    return ResponseCode(11)
            else:
                return ResponseCode(9)

    async def get_file(self):
        file_list = list()
        async with JobDb() as pool:
            board_id = await pool.fetchrow(sql.CHECK_BOARD, self.boald, self.user_id)
            if board_id:
                all_file_board = await pool.fetch(sql.GET_FILE, self.user_id, board_id['id'])
                if all_file_board:
                    for i_file in all_file_board:
                        file = Userfile(**i_file)
                        file_list.append(file)
                    return ResponseCodeData(1, {self.boald:file_list})
                return ResponseCodeData(1, {self.boald:all_file_board})
            else:
                return ResponseCode(9)

    async def delete_file(self, file_name):
        async with JobDb() as pool:
            board_id = await pool.fetchrow(sql.CHECK_BOARD, self.boald, self.user_id)
            if board_id:
                all_file_board = await pool.fetch(sql.CHECK_FILE, file_name, self.user_id)
                if all_file_board:
                    await pool.fetch(sql.DETETE_FILE, self.user_id, board_id['id'], file_name)
                    return ResponseCode(1)
                else:
                    ResponseCode(12)
            else:
                return ResponseCode(9)

    async def rename_file(self,  file_old_name: str, file_new_name: str):
        async with JobDb() as pool:
            board_id = await pool.fetchrow(sql.CHECK_BOARD, self.boald, self.user_id)
            if board_id:
                all_file_board = await pool.fetch(sql.CHECK_FILE, file_old_name, self.user_id)
                if all_file_board:
                    await pool.fetch(sql.RENAME_FILE, file_new_name, self.user_id, file_old_name, board_id['id'])
                    return ResponseCode(1)
                else:
                    return ResponseCode(12)
            else:
                return ResponseCode(9)

    async def update_file(self, name_file: str, contetn: str):
        async with JobDb() as pool:
            board_id = await pool.fetchrow(sql.CHECK_BOARD, self.boald, self.user_id)
            if board_id:
                all_file_board = await pool.fetch(sql.CHECK_FILE, name_file, self.user_id)
                if all_file_board:
                    await pool.fetch(sql.UPDATE_CONTETN, contetn, self.user_id, name_file, board_id['id'])
                    return ResponseCode(1)
                else:
                    return ResponseCode(12)
            else:
                return ResponseCode(9)
