import sqlite3
from sqlite3 import Error
import logging


"""
Уровни логирования: 

Debug (10): самый низкий уровень логирования, предназначенный для отладочных сообщений, для вывода диагностической информации о приложении.

Info (20): этот уровень предназначен для вывода данных о фрагментах кода, работающих так, как ожидается.

Warning (30): этот уровень логирования предусматривает вывод предупреждений, он применяется для записи сведений о событиях, на которые программист обычно обращает внимание. Такие события вполне могут привести к проблемам при работе приложения. Если явно не задать уровень логирования — по умолчанию используется именно warning.

Error (40): этот уровень логирования предусматривает вывод сведений об ошибках — о том, что часть приложения работает не так как ожидается, о том, что программа не смогла правильно выполниться.

Critical (50): этот уровень используется для вывода сведений об очень серьёзных ошибках, наличие которых угрожает нормальному функционированию всего приложения. Если не исправить такую ошибку — это может привести к тому, что приложение прекратит работу.
"""

'''Задание.
Требуется создать БД, состоящую из четырех таблиц:
1.  users
2.  posts
3.  comments
4.  likes
Пользователи (users) и публикации (posts) будут находиться иметь тип связи один-ко-многим:
одному читателю может понравиться несколько постов.
Точно так же один и тот же юзер может оставлять много комментариев (comments), а
один пост может иметь несколько комментариев.
Таким образом, и users, и posts по отношению к comments имеют тот же тип связи.
Лайки (likes) в этом плане идентичны комментариям.
'''

def create_connection(path):
    '''создание подключения к базе данных'''
    connection = None
    try:
        connection = sqlite3.connect(path)
        logging.info("Connection to SQLite DB successful")
    except Error as e:
        logging.error(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query):
    '''выполнение запросов'''
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        logging.info("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    '''Извлечение данных из записей'''
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


connection = create_connection(":memory:")

'''Запрос для создания таблицы users'''
create_users_table = """
                    CREATE TABLE IF NOT EXISTS users (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT NOT NULL,
                          age INTEGER,
                          gender TEXT,
                          nationality TEXT
                    );"""

'''запрос для создания таблицы posts'''
create_posts_table = """
                    CREATE TABLE IF NOT EXISTS posts(
                          id INTEGER PRIMARY KEY AUTOINCREMENT, 
                          title TEXT NOT NULL, 
                          description TEXT NOT NULL, 
                          user_id INTEGER NOT NULL, 
                          FOREIGN KEY (user_id) REFERENCES users (id)
                    );"""


'''таблицы comments и likes'''
create_comments_table = """
                    CREATE TABLE IF NOT EXISTS comments (
                          id INTEGER PRIMARY KEY AUTOINCREMENT, 
                          text TEXT NOT NULL, 
                          user_id INTEGER NOT NULL, 
                          post_id INTEGER NOT NULL, 
                          FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
                    );"""

create_likes_table = """
                    CREATE TABLE IF NOT EXISTS likes (
                          id INTEGER PRIMARY KEY AUTOINCREMENT, 
                          user_id INTEGER NOT NULL, 
                          post_id integer NOT NULL, 
                          FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
                    );"""


'''выполнение запровов по созданию таблиц'''
execute_query(connection, create_users_table)
execute_query(connection, create_posts_table)
execute_query(connection, create_comments_table)
execute_query(connection, create_likes_table)

'''Вставка данных'''
create_users = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""

execute_query(connection, create_users)

create_posts = """
INSERT INTO
  posts (title, description, user_id)
VALUES
  ("Happy", "I am feeling very happy today", 1),
  ("Hot Weather", "The weather is very hot today", 2),
  ("Help", "I need some help with my work", 2),
  ("Great News", "I am getting married", 1),
  ("Interesting Game", "It was a fantastic game of tennis", 5),
  ("Party", "Anyone up for a late-night party today?", 3);
"""

execute_query(connection, create_posts)

create_comments = """
INSERT INTO
  comments (text, user_id, post_id)
VALUES
  ('Count me in', 1, 6),
  ('What sort of help?', 5, 3),
  ('Congrats buddy', 2, 4),
  ('I was rooting for Nadal though', 4, 5),
  ('Help with your thesis?', 2, 3),
  ('Many congratulations', 5, 4);
"""

create_likes = """
INSERT INTO
  likes (user_id, post_id)
VALUES
  (1, 6),
  (2, 3),
  (1, 5),
  (5, 4),
  (2, 4),
  (4, 2),
  (3, 6);
"""

execute_query(connection, create_comments)
execute_query(connection, create_likes)

'''выберем все записи из таблицы users:'''
select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)


"""
users = [
    (1, 'James', 25, 'male', 'USA'), 
    (2, 'Leila', 32, 'female', 'France'),
    (3, 'Brigitte', 35, 'female', 'England')
]

output: ['James', 'Leila', 'Brigitte']

[for list(name) in users]

"""

users_gen = [list(name)[1] for name in users if type(list(name)[1]) == str]


select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)

select_posts= "SELECT * from posts"
posts = execute_read_query(connection, select_posts)
# for user in users:
#     print(user)
#
# print()
# for post in posts:
#     print(post)

# create_users_table = """
#                     CREATE TABLE IF NOT EXISTS users (
#                           id INTEGER PRIMARY KEY AUTOINCREMENT,
#                           name TEXT NOT NULL,
#                           age INTEGER,
#                           gender TEXT,
#                           nationality TEXT
#                     );"""
#
# '''запрос для создания таблицы posts'''
# create_posts_table = """
#                     CREATE TABLE IF NOT EXISTS posts(
#                           id INTEGER PRIMARY KEY AUTOINCREMENT,
#                           title TEXT NOT NULL,
#                           description TEXT NOT NULL,
#                           user_id INTEGER NOT NULL,
#                           FOREIGN KEY (user_id) REFERENCES users (id)
#                     );"""


sql = """
select 
    users.id,
    users.name,
    posts.description
from 
    posts INNER JOIN users
on
    users.id = posts.user_id
"""

# select_users_posts = execute_read_query(connection, sql)
# for select_users_post in select_users_posts:
#     print(select_users_post)
# sql = """
# select * from likes;
# """
#
# select_users_posts = execute_read_query(connection, sql)
# for select_users_post in select_users_posts:
#     print(select_users_post)

sql = """
SELECT
    description as Post,
    count(likes.id) as Likes
FROM
    likes,
    posts
WHERE
    posts.id = likes.post_id
GROUP BY
    likes.post_id
"""

"""
post_id   desc    likes
1         ..       3
2         ..       4 
3         ..       5

"""

select_users_posts = execute_read_query(connection, sql)
for select_users_post in select_users_posts:
    print(select_users_post)