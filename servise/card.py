from database.connection_db import JobDb

from database.parameter_schemes import UserCatd, UserCardOut, UserCardContent

import database.sql_requests as sql
from response_code import ResponseCode, ResponseCodeData


class File:
    def __init__(self, boardId: int, user: int):
        self.user_id: int = user
        self.board: int = boardId

    async def create_card(self, card_name: str):
        try:
            async with JobDb() as pool:
                board_id = await pool.fetchrow(sql.CHECK_BOARD, None, self.user_id, self.board)
                if board_id:
                    check_file = await pool.fetchrow(sql.CHECK_CARD, card_name, self.user_id, None)
                    if check_file is None:
                        file = await pool.fetchrow(sql.NEW_CARD, self.user_id, board_id['id'], card_name)
                        file = UserCardOut(**file)
                        return ResponseCodeData(1, file)
                    else:
                        return ResponseCode(11)
                else:
                    return ResponseCode(9)
        except Exception as exc:
            return ResponseCode(7)

    async def get_card(self):
        try:
            file_list = list()
            async with JobDb() as pool:
                board_id = await pool.fetchrow(sql.CHECK_BOARD, None, self.user_id, self.board)
                if board_id:
                    all_card_board = await pool.fetch(sql.GET_CARD, self.user_id, board_id['id'])
                    print(all_card_board)
                    if all_card_board:
                        for i_file in all_card_board:
                            file = UserCatd(**i_file)
                            file_list.append(file)
                        return ResponseCodeData(1, {self.board:file_list})
                    return ResponseCodeData(1, {self.board:all_card_board})
                else:
                    return ResponseCode(9)
        except Exception as exc:
            return ResponseCode(7)

    async def delete_file(self, boarId: int):
        try:
            async with JobDb() as pool:
                board_id = await pool.fetchrow(sql.CHECK_BOARD, None, self.user_id, self.board)
                if board_id:
                    all_file_board = await pool.fetch(sql.CHECK_CARD, None, self.user_id, boarId)
                    if all_file_board:
                        await pool.fetch(sql.DETETE_FILE, self.user_id, board_id['id'], boarId)
                        return ResponseCode(1)
                    else:
                        return ResponseCode(12)
                else:
                    return ResponseCode(9)
        except Exception as exc:
            return ResponseCode(7)

    async def rename_card(self,  fileId: int, card_new_name: str):
        try:
            async with JobDb() as pool:
                board_id = await pool.fetchrow(sql.CHECK_BOARD, None, self.user_id, self.board)
                if board_id:
                    all_file_board = await pool.fetch(sql.CHECK_CARD, None, self.user_id, fileId)
                    if all_file_board:
                        file = await pool.fetch(sql.RENAME_FILE, card_new_name, self.user_id, fileId, board_id['id'])
                        file = UserCardOut(**file[0])
                        return ResponseCodeData(1, file)
                    else:
                        return ResponseCode(12)
                else:
                    return ResponseCode(9)
        except Exception as exc:
            return ResponseCode(7)

    async def add_card(self, cardId: int, contetn: str):
        try:
            async with JobDb() as pool:
                board_id = await pool.fetchrow(sql.CHECK_BOARD, None, self.user_id, self.board)
                if board_id:
                    all_file_board = await pool.fetch(sql.CHECK_CARD, None, self.user_id, cardId)
                    if all_file_board:
                        card = await pool.fetch(sql.UPDATE_CONTETN, contetn, self.user_id, cardId, board_id['id'])
                        card = UserCardContent(**card[0])
                        return ResponseCodeData(1, card)
                    else:
                        return ResponseCode(12)
                else:
                    return ResponseCode(9)
        except Exception as exc:
            return ResponseCode(7)

    async def get_card_content(self, cardId: int):
        try:
            async with JobDb() as pool:
                board_id = await pool.fetchrow(sql.CHECK_BOARD, None, self.user_id, self.board)
                if board_id:
                    all_file_board = await pool.fetch(sql.CHECK_CARD, None, self.user_id, cardId)
                    if all_file_board:
                        card = await pool.fetch(sql.GET_CONTENT, self.user_id, board_id['id'], cardId)
                        card = UserCardContent(**card[0])
                        return ResponseCodeData(1, card)
                    else:
                        return ResponseCode(12)
                else:
                    return ResponseCode(9)
        except Exception as exc:
            return ResponseCode(7)


