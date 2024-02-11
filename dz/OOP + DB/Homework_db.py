import sqlite3

file = r'C:\Users\admin\PycharmProjects\Base_\User.db'

conn = sqlite3.connect(file)
cur = conn.cursor()



""" USER """

values = [(1, "Kirill", 16),(2, "Roma", 13),(3, "Nikita", 22),(4, "Sasha", 15),(5, "Max", 14)]
cur.executemany("""INSERT INTO user (id, name, age) VALUES (?, ?, ?)""", values)

""" PICTURE """

values = [(2, "C:", "1280x720"),(1, "C:", "1920x1080"),(4, "C:", "720x576"),(5, "C:", "640x480"),(3, "C:", "3840x2160")]
cur.executemany("""INSERT INTO user_pic (id, file_path, resolution) VALUES (?, ?, ?)""", values)

""" FRIEND """

values = [(2, "Vany"),(1, "Mark"),(4, "Timon"),(4, "Serega"),(5, "Sasha"),(3, "Petr"),(1, "Kosty"),(1, "Egor"),(2, "Koly")]
cur.executemany("""INSERT INTO friend (id, name) VALUES (?, ?)""", values)

""" INTERESTI"""

values = [(2, "Tennis"),(1, "Volleyboll"),(3, "Programmer"),(5, "Judo"),(4, "Karate")]
cur.executemany("""INSERT INTO interest (id, interest) VALUES (?, ?)""", values)

""" CONNECTIVE """

values = [(1,1,1,1),(3,3,3,3),(2,2,2,2),(5,5,5,5),(4,4,4,4)]
cur.executemany("""INSERT INTO user_connective (user_id, pic_id, friend_id, interest_id) VALUES (?, ?, ?, ?)""", values)

conn.commit()