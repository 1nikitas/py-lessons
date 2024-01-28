"""
Объяснения изменений:

1. DataBase класс: Создан для обработки всех операций с базой данных.
2. execute_sql: Общий метод для выполнения SQL-запросов с параметрами, защищает от SQL-инъекций.
3 .user_exists: Проверка существования пользователя.
4. respond: Стандартизированный способ ответа на действия пользователя.
5. Использование параметризованных запросов: Это предотвращает SQL-инъекции.
6. Иерархия классов: User, Moderator, и Admin наследуются от DataBase и используют его методы для взаимодействия с базой данных.
"""

import sqlite3

class DataBase:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def execute_sql(self, sql, params=()):
        with self.connection:
            self.cursor.execute(sql, params)
            return self.cursor.fetchall()

    def user_exists(self, name, age, id):
        sql = "SELECT 1 FROM RegOnServer WHERE name = ? AND age = ? AND id = ?"
        return bool(self.execute_sql(sql, (name, age, id)))

    def respond(self, success, name):
        if success:
            return f'Пользователь {name} успешно обновлен.'
        return f'Пользователя {name} не существует.'


class User(DataBase):
    def __init__(self, db_file, id, name, age, role):
        super().__init__(db_file)
        self.id = id
        self.name = name
        self.age = age
        self.role = role

    def add_user(self):
        if self.user_exists(self.name, self.age, self.id):
            return 'Пользователь с таким именем уже существует!'

        sql = "INSERT INTO RegOnServer (id, name, age, role) VALUES (?, ?, ?, ?)"
        self.execute_sql(sql, (self.id, self.name, self.age, self.role))
        return f"Пользователь создан) id: {self.id}, Имя: {self.name}, Возраст: {self.age}, Роль: {self.role}"


class Moderator(User):
    def delete_user(self, name, age, id):
        if self.user_exists(name, age, id):
            sql = "DELETE FROM RegOnServer WHERE name = ? AND age = ? AND id = ?"
            self.execute_sql(sql, (name, age, id))
            return f'Пользователь под именем {name} был удалён из базы.'
        return self.respond(False, name)

    def update_user(self, *, user, id, name, age):
        if self.user_exists(user.name, user.age, user.id):
            sql = "UPDATE RegOnServer SET name = ?, id = ?, age = ? WHERE name = ? AND id = ? AND age = ?"
            self.execute_sql(sql, (name, id, age, user.name, user.id, user.age))
            return self.respond(True, name)
        return self.respond(False, name)


class Admin(Moderator):
    def add_moderator(self, moderator):
        return moderator.add_user()

    def add_admin(self):
        return self.add_user()

    def clean_all(self):
        self.execute_sql("DELETE FROM RegOnServer")
        return "База успешно очищена!"


# Пример использования:
db_file = r'C:\Users\admin\Desktop\lessons\example_db'
kirill_admin = Admin(db_file=db_file, id=0, name="Кирилл", age=16, role="Admin")
response = kirill_admin.add_admin()
print(response)
