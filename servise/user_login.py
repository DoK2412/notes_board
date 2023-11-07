from database.connection_db import JobDb

import database.sql_requests as sql
from database.parameter_schemes import UserProfile

from response_code import ResponseCode, ResponseCodeData


async def authorization(request, username, password):
    try:
        async with JobDb() as pool:
            user = await pool.fetchrow(sql.ADD_USER, username)
            if user:
                if user['password'] != str(password):
                    return ResponseCode(3)
                else:
                    return ResponseCodeData(1, {'userId': user['id'], 'userName': user['user_name']})
            else:
                return ResponseCode(8)
    except Exception as exc:
        return ResponseCode(7)


async def registrations(request, username, password, passwordConfig):
    try:
        if password != passwordConfig:
            return ResponseCode(4)
        async with JobDb() as pool:
            user = await pool.fetchrow(sql.ADD_USER, username)
            if user:
                return ResponseCode(5)

            users = await pool.fetchrow(sql.NEW_USER, username, password)
            return ResponseCodeData(1, {'userId': users['id'], 'userName': users['user_name']})
    except Exception as exc:
        return ResponseCode(7)


async def get_profile(request, user_id):
    try:
        async with JobDb() as pool:
            user = await pool.fetchrow(sql.GET_PROFILE, user_id)
            if user:
                profile = UserProfile(**user)
                return ResponseCodeData(1, profile)
            else:
                return ResponseCode(8)

    except Exception as exc:
        return ResponseCode(7)
