"""
Можно улучшить в коде:
1. Использование f-строк для SQL-запросов: Это может привести к SQL-инъекциям.
2. Лучше использовать параметризованные запросы.
3. Дублирование кода: В функциях delete_user, update_user, add_user, add_moder, и add_admin есть повторяющиеся части кода, которые можно вынести в отдельные методы.
4. Проверка пользователя: Проверка существования пользователя происходит в каждом методе. Можно создать отдельный метод для этого.
5. Именование методов и переменных: Следует использовать более описательные имена, чтобы код был понятен.
6. Использование транзакций: Чтобы обеспечить целостность данных, лучше использовать контекстный менеджер для транзакций.
7. Ненужная инициализация базового класса: В Python 3 можно использовать super().__init__() без аргументов.
"""


import sqlite3

file = r'C:\Users\admin\Desktop\lessons\example_db'

class ChangeDataBase:
    def __init__(self, file=file):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

    def change(self, sql):
        with self.connection:
            self.cursor.execute(sql)
            self.connection.commit()

class User(ChangeDataBase):
    def __init__(self, *, id, name, age, role, file=file):
        ChangeDataBase.__init__(self, file)
        self.id = id
        self.name = name
        self.age = age
        self._role = role

    @property
    def role(self):
        return self._role

    def check_user(self, name, age, id):
        with self.connection:
            sql = f"SELECT id FROM RegOnServer WHERE name = '{name}' AND age = {age} AND id = {id}"
            self.cursor.execute(sql)
            select_name = self.cursor.fetchone()

            if not(select_name):
                 return False

            return bool(len(select_name))

    def hasnt_user(self, name):
        return f'Пользователя {name} не существует.'


class BaseUser(User):
    def add_user(self):
        if super().check_user(self.name, self.age, self.id):
            return 'Пользователь с таким именем уже существует!'

        sql = f"INSERT INTO RegOnServer (id, name, age, role) VALUES ({self.id}, '{self.name}', {self.age}, '{self.role}')"
        super().change(sql)
        return f"Пользователь создан) id: {self.id}, Имя: {self.name}, Возраст: {self.age}, Роль: {self._role}"

roma_basic1 = BaseUser(id=100, name="Рома", age=12, role="User")
roma_basic2 = BaseUser(id=40,name="Рома", age=13, role="User")
roma_basic2.add_user()



class Moderator(User):
    def delete_user(self, name, age, id):
        if super().check_user(name, age, id):
            sql = f"DELETE FROM RegOnServer WHERE name = '{name}' AND age = {age}"
            super().change(sql)
            return f'Пользователь под именем {name} был удалён из базы.'
        super().hasnt_user(name)

    def update_user(self, *, user, id, name, age):
        if super().check_user(name, age, id):
            sql = f"UPDATE RegOnServer SET name = '{name}', id = {id}, age = {age} WHERE name = '{user.name}' AND id = {user.id} AND age = {user.age}"
            super().change(sql)
            return f'Пользователь успешно изменён. id: {id}, Имя: {name}, Возраст: {age}'
        super().hasnt_user(name)

robot1 = Moderator(id=-1, name="Валли", age=1, role="Moderator")
robot2 = Moderator(id=-2, name="Коп", age=2, role="Moderator")

class Admin(User):
    def delete_user(self, *, name, age, id):
        if super().check_user(name, age, id):
            sql = f"DELETE FROM RegOnServer WHERE name = '{name}' AND age = {age} AND id = {id}"
            super().change(sql)
            return f'Пользователь под именем {name} был удалён из базы.'
        super().hasnt_user(name)

    def update_user(self, *, user, id, name, age):
        if super().check_user(user.name, user.age, user.id):
            sql = f"UPDATE RegOnServer SET name = '{name}', id = {id}, age = {age} WHERE name = '{user.name}' AND id = {user.id} AND age = {user.age}"
            super().change(sql)
            return f'Пользователь успешно изменён. id: {id}, Имя: {name}, Возраст: {age}'
        super().hasnt_user(name)

    def add_moder(self, moderator):
        if super().check_user(moderator.name, moderator.age, moderator.id):
            return 'Модератор с таким именем уже существует!'

        sql = f"INSERT INTO RegOnServer (id, name, age, role) VALUES ({moderator.id}, '{moderator.name}', {moderator.age}, '{moderator.role}')"
        super().change(sql)
        return f"Модератор создан) id: {moderator.id}, Имя: {moderator.name}, Возраст: {moderator.age}, Роль: {moderator._role}"

    def add_admin(self):
        if super().check_user(self.name, self.age, self.id):
            return 'Админ с таким именем уже существует!'

        sql = f"INSERT INTO RegOnServer (id, name, age, role) VALUES ({self.id}, '{self.name}', {self.age}, '{self.role}')"
        super().change(sql)
        return f"Модератор создан) id: {self.id}, Имя: {self.name}, Возраст: {self.age}, Роль: {self._role}"

    def clean_all(self):
        sql = f"DELETE FROM RegOnServer"
        super().change(sql)
        return "База успешно очищена!"


kirill_admin = Admin(id=0, name="Кирилл", age=16, role="Admin")
roma_admin = Admin(id=0, name="Роман", age=13, role="Admin")

kirill_admin.add_admin()
roma_admin.add_admin()

kirill_admin.add_moder(robot1)
roma_admin.add_moder(robot2)

print(kirill_admin.update_user(user=roma_basic2, id=888, name="Никита", age=20))
