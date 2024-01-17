from typing import Any

response = {
    1: 'Успешное выполнение запроса ',
    2: 'Авторизация не пройдена',
    3: 'Логин или пароль не совпадает',
    4: 'Пароли не совпадают',
    5: 'Пользователь есть в базе данных',
    6: 'Пользователь создан в базе данных',

    7: 'Ошибка на стороне сервера',
    8: 'Пользователь не найден',

    9: 'У пользователя нет рабочих пространств',
    10: 'Рабочее пространство с таким именем уже существует',

    11: 'У пользователя уже есть файл с данным именем',
    12: 'У пользователя нет указанной карточки',

    13: "У пользователя нет рабочего пространства с таким именем",
    14: "У пользователя уже есть такое название в списке",
    15: "У пользователя нет записей в списке"
}
Response = {
    "/authentication": [1, 3, 7, 8],
    "/registration": [1, 4, 5, 7],
    "/profile": [1, 2, 7, 8],
    "/createBoard": [1, 2, 7, 10],
    "/deleteBoard": [1, 2, 7, 9],
    "/getBoard": [1, 2, 7, 9],
    "/renameBoard": [1, 2, 7, 9],
    "/createFile": [1, 2, 7, 9, 11],
    "/getFile": [1, 2, 7, 9],
    "/deleteFile": [1, 2, 7, 9, 11],
    "/renameFile": [1, 2, 7, 9, 12],
    "/updateFile": [1, 2, 7, 9, 12],
    "/createList": [1, 2, 13, 12, 13, 14],
    "/getList": [1, 2, 7, 12, 13],
    "/deleteList": [1, 2, 7, 12, 13],
    "/addContentList": [1, 2, 7, 12, 13],
    "/getContentList": [1, 2, 7, 12, 13]
}

class ResponseCode():
    def __init__(self, code, data=None):
        self.answercode: int = code
        self.answer: str = response[code]

class ResponseCodeData():
    def __init__(self, code, data):
        self.answercode: int = code
        self.answer: str = response[code]
        self.data: Any = data

