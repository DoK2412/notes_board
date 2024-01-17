from database.connection_db import JobDb

from database.parameter_schemes import UserCatd, UserCardOut, UserCardContent, UserListdOut, UserList

import database.sql_requests as sql
from response_code import ResponseCode, ResponseCodeData


class Lists:
    def __init__(self, boardId: int, user: int, cardId: int):
        self.user_id: int = user
        self.board: int = boardId
        self.card: int = cardId

    async def create_list(self, list_name: str):
        try:
            async with JobDb() as pool:
                board_id = await pool.fetchrow(sql.CHECK_BOARD, None, self.user_id, self.board)
                if board_id is None:
                    return ResponseCode(13)
                check_file = await pool.fetchrow(sql.CHECK_CARD, None, self.user_id, self.card)
                if check_file is None:
                    return ResponseCode(12)
                if board_id and check_file:
                    check_list = await pool.fetchrow(sql.CHECK_LIST, list_name, self.board, self.user_id, self.card, None)
                    if check_list is None:
                        list = await pool.fetchrow(sql.NEW_LIST, self.user_id, self.board, self.card, list_name)
                        list = UserListdOut(**list)
                        return ResponseCodeData(1, list)
                    else:
                        return ResponseCode(14)
        except Exception as exc:
            return ResponseCode(7)

    async def get_list(self):
        try:
            async with JobDb() as pool:
                board_id = await pool.fetchrow(sql.CHECK_BOARD, None, self.user_id, self.board)
                if board_id is None:
                    return ResponseCode(13)
                check_file = await pool.fetchrow(sql.CHECK_CARD, None, self.user_id, self.card)
                if check_file is None:
                    return ResponseCode(12)
                if board_id and check_file:
                    all_list_card = await pool.fetch(sql.GET_LIST, self.user_id, self.board, self.card)
                    if all_list_card:
                        all_list = list()
                        for i_list in all_list_card:
                            lists = UserList(**i_list)
                            all_list.append(lists)
                        return ResponseCodeData(1, all_list)
                    else:
                        return ResponseCode(15)
        except Exception as exc:
            return ResponseCode(7)

    async def delete_list(self, listId: int):
        try:
            async with JobDb() as pool:
                board_id = await pool.fetchrow(sql.CHECK_BOARD, None, self.user_id, self.board)
                if board_id is None:
                    return ResponseCode(13)
                check_file = await pool.fetchrow(sql.CHECK_CARD, None, self.user_id, self.card)
                if check_file is None:
                    return ResponseCode(12)
                if board_id and check_file:
                    await pool.fetch(sql.DETETE_LIST, self.user_id, self.board, listId)
                    return ResponseCode(1)
        except Exception as exc:
            return ResponseCode(7)

    async def rename_list(self,  listId: int, list_new_name: str):
        try:
            async with JobDb() as pool:
                board_id = await pool.fetchrow(sql.CHECK_BOARD, None, self.user_id, self.board)
                if board_id is None:
                    return ResponseCode(13)
                check_file = await pool.fetchrow(sql.CHECK_CARD, None, self.user_id, self.card)
                if check_file is None:
                    return ResponseCode(12)
                if board_id and check_file:
                    lists = await pool.fetchrow(sql.RENAME_LIST, list_new_name, self.user_id, listId, self.board, self.card)
                    lists = UserListdOut(**lists)
                    return ResponseCodeData(1, lists)
        except Exception as exc:
            return ResponseCode(7)

    async def add_list_content(self, cardId: int, content: str):
        try:
            async with JobDb() as pool:
                board_id = await pool.fetchrow(sql.CHECK_BOARD, None, self.user_id, self.board)
                if board_id is None:
                    return ResponseCode(13)
                check_file = await pool.fetchrow(sql.CHECK_CARD, None, self.user_id, self.card)
                if check_file is None:
                    return ResponseCode(12)
                if board_id and check_file:
                    lists = await pool.fetch(sql.UPDATE_CONTETN, content, self.user_id, cardId, self.board, self.card)
                    lists = UserCardContent(**lists[0])
                    return ResponseCodeData(1, lists)
        except Exception as exc:
            return ResponseCode(7)

    async def get_list_content(self, listId: int):
        try:
            async with JobDb() as pool:
                board_id = await pool.fetchrow(sql.CHECK_BOARD, None, self.user_id, self.board)
                if board_id is None:
                    return ResponseCode(13)
                check_file = await pool.fetchrow(sql.CHECK_CARD, None, self.user_id, self.card)
                if check_file is None:
                    return ResponseCode(12)
                if board_id and check_file:
                    lists = await pool.fetch(sql.GET_CONTENT, self.user_id, self.board, self.card, listId)
                    lists = UserCardContent(**lists[0])
                    return ResponseCodeData(1, lists)
        except Exception as exc:
            return ResponseCode(7)


