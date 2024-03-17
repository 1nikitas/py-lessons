import sqlite3


def connection(file):
    '''создание подключения к базе данных'''
    connection = sqlite3.connect(file)
    return connection


def execute(connection, sql):
    '''выполнение запросов'''
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()


connection = connection(r"D:\SQL db\Finance")

