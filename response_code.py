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

    9: 'У пользователя нет рабочего пространства с таким именем',
    10: 'Рабочее простарнство с таким именем уже существует',

    11: 'У пользователя уже есть файл с данным именем',
    12: 'У пользователя нет указанного файла'

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
