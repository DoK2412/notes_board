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
SELECT id FROM alena_servis.board 
WHERE
    CASE WHEN bool($1::varchar is not null) THEN name_board = $1::varchar ELSE true END
    AND CASE WHEN bool($2::integer is not null) THEN user_id = $2::integer ELSE true END
    AND CASE WHEN bool($3::integer is not null) THEN id = $3::integer ELSE true END
'''

NEW_BOARD = '''
--создание рабочего пространства пользователя
INSERT INTO alena_servis.board
    (user_id, name_board)
VALUES 
    ($1, $2) RETURNING id as "boardId", name_board as "nameBoard"
'''

GET_BOARD = '''
--получене списка досок
SELECT id as "boardId", name_board as "nameBoard" FROM alena_servis.board WHERE user_id = $1
'''

RENAME_BOLDER = '''
--переименование рабочего пространства
UPDATE alena_servis.board SET name_board = $1 WHERE user_id = $2 and id = $3 RETURNING id, name_board as "nameBoard"
'''

DETETE_BOARD = '''
--удаление рабочего пространства пользователя
DELETE FROM alena_servis.board WHERE id = $2 and user_id = $1
'''

DETETE_BOARD_FILE = '''
--удаление карточки из рабочей дерриктории
DELETE FROM alena_servis.card WHERE board_id = $2 AND user_id = $1
'''

CHECK_CARD = '''
--проверка наличия карточки
SELECT id FROM alena_servis.card WHERE
    CASE WHEN bool($1::varchar is not null) THEN card_name = $1::varchar ELSE true END
    AND CASE WHEN bool($2::integer is not null) THEN user_id = $2::integer ELSE true END
    AND CASE WHEN bool($3::integer is not null) THEN id = $3::integer ELSE true END

'''

NEW_CARD = '''
--создание карточки в рабочем пространстве пользователя
INSERT INTO alena_servis.card
    (user_id, board_id, card_name)
VALUES 
    ($1, $2, $3) RETURNING id as "cardId", board_id as "boardId", card_name as "nameCard"
'''

GET_CARD = '''
--получене списка карточки
SELECT id as "cardId", board_id as "boardId", card_name as "nameCard" FROM alena_servis.card WHERE user_id = $1 AND board_id = $2
'''

DETETE_FILE = '''
--удаление карточки из рабочей дерриктории
DELETE FROM alena_servis.card WHERE board_id = $2 AND user_id = $1 AND id = $3
'''

RENAME_FILE = '''
--переименование карточки
UPDATE alena_servis.card SET card_name = $1 WHERE user_id = $2 and id = $3 and board_id = $4 RETURNING id as "cardId", board_id as "boardId", card_name as "nameCard"
'''

UPDATE_CONTETN = '''
--переименование карточки
UPDATE alena_servis.list SET content = $1 WHERE user_id = $2 and id = $3 and board_id = $4 and card_id = $5 RETURNING id as "listId", list_name as "namelist", content
'''

GET_PROFILE = '''
--получение профиля пользователя
SELECT id, user_name as "userName" FROM alena_servis.profile WHERE id = $1'''

GET_CONTENT = '''
--получение данных карточки
SELECT id as "listId", list_name as "namelist", content FROM alena_servis.list WHERE user_id = $1 AND board_id = $2 AND card_id = $3 AND id = $4
 
'''


CHECK_LIST = '''
--проверка файла в списке

SELECT id FROM alena_servis.list WHERE
    CASE WHEN bool($1::varchar is not null) THEN list_name = $1::varchar ELSE true END
    AND CASE WHEN bool($2::integer is not null) THEN board_id = $2::integer ELSE true END
    AND CASE WHEN bool($3::integer is not null) THEN user_id = $3::integer ELSE true END
    AND CASE WHEN bool($4::integer is not null) THEN card_id = $4::integer ELSE true END
    AND CASE WHEN bool($5::integer is not null) THEN id = $5::integer ELSE true END
'''

NEW_LIST = '''
--создание списка в карточке пользователя
INSERT INTO alena_servis.list
    (user_id, board_id, card_id, list_name)
VALUES 
    ($1, $2, $3, $4) RETURNING id as "listId", list_name as "nameList"
'''

GET_LIST = '''
--получене списка из карточки
SELECT id as "listId", list_name as "nameList" FROM alena_servis.list WHERE user_id = $1 AND board_id = $2 AND card_id = $3
'''

DETETE_LIST = '''
--удаление данных из списка
DELETE FROM alena_servis.list WHERE board_id = $2 AND user_id = $1 AND id = $3
'''

RENAME_LIST = '''
--переименование данных в списке
UPDATE alena_servis.list SET list_name = $1 WHERE user_id = $2 and id = $3 and board_id = $4 and card_id = $5 RETURNING id as "listId", list_name as "nameList"
'''