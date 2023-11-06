ADD_USER = '''
--получение данных о пользователя
SELECT id, user_name, password FROM alena_servis.profile WHERE user_name = $1
'''

NEW_USER = '''
--добавление нового пользователя
INSERT INTO alena_servis.profile
    (user_name, password)
VALUES 
    ($1, $2) RETURNING id, user_name
'''

CHECK_BOARD = '''
--проверка рабочего пространства пользоватля
SELECT id FROM alena_servis.board WHERE name_board = $1 and user_id = $2
'''

NEW_BOARD = '''
--создание рабочего пространства пользователя
INSERT INTO alena_servis.board
    (user_id, name_board)
VALUES 
    ($1, $2) RETURNING id
'''

GET_BOARD = '''
--получене списка досок
SELECT id, name_board as "nameBoard" FROM alena_servis.board WHERE user_id = $1
'''

RENAME_BOLDER = '''
--переименование рабочего пространства
UPDATE alena_servis.board SET name_board = $1 WHERE user_id = $2 and name_board = $3
'''

DETETE_BOARD = '''
--удаление рабочего пространства пользователя
DELETE FROM alena_servis.board WHERE name_board = $2 and user_id = $1
'''

DETETE_BOARD_FILE = '''
--удаление файла из рабочей дерриктории
DELETE FROM alena_servis.file WHERE board_id = $2 AND user_id = $1
'''

CHECK_FILE = '''
--проверка наличия файла
SELECT id FROM alena_servis.file WHERE name_file = $1 and user_id = $2
'''

NEW_FILE = '''
--создание файла в рабочем пространстве пользователя
INSERT INTO alena_servis.file
    (user_id, board_id, name_file, content)
VALUES 
    ($1, $2, $3, $4) RETURNING id
'''

GET_FILE = '''
--получене списка файлов
SELECT id, board_id as "boardId", content, name_file as "nameFile" FROM alena_servis.file WHERE user_id = $1 AND board_id = $2
'''

DETETE_FILE = '''
--удаление файла из рабочей дерриктории
DELETE FROM alena_servis.file WHERE board_id = $2 AND user_id = $1 AND name_file = $3
'''

RENAME_FILE = '''
--переименование файла
UPDATE alena_servis.file SET name_file = $1 WHERE user_id = $2 and name_file = $3 and board_id = $4
'''

UPDATE_CONTETN = '''
--переименование файла
UPDATE alena_servis.file SET content = $1 WHERE user_id = $2 and name_file = $3 and board_id = $4
'''

GET_PROFILE = '''
--получение профиля пользователя
SELECT id, user_name as "userName" FROM alena_servis.profile WHERE id = $1'''