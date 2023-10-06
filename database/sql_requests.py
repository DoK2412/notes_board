ADD_USER = '''
--получение данных о пользователя
SELECT id, user_name, password FROM alena_servis.user_servis_alena WHERE user_name = $1
'''

NEW_USER = '''
--добавление нового пользователя
INSERT INTO alena_servis.user_servis_alena
    (user_name, password)
VALUES 
    ($1, $2) RETURNING id
'''

CHECK_BOARD = '''
--проверка рабочего пространства пользоватля
SELECT id FROM alena_servis.doska WHERE name_doska = $1 and user_id = $2
'''

NEW_BOARD = '''
--создание рабочего пространства пользователя
INSERT INTO alena_servis.doska
    (user_id, name_doska)
VALUES 
    ($1, $2) RETURNING id
'''

GET_BOARD = '''
--получене списка досок
SELECT * FROM alena_servis.doska WHERE user_id = $1
'''

RENAME_BOLDER = '''
--переименование рабочего пространства
UPDATE alena_servis.doska SET name_doska = $1 WHERE user_id = $2 and name_doska = $3
'''

DETETE_BOARD = '''
--удаление рабочего пространства пользователя
DELETE FROM alena_servis.doska WHERE name_doska = $2 and user_id = $1
'''
