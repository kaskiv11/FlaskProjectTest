import sqlite3

connection = sqlite3.connect("database.db")

with open('schema.sql') as file:
    connection.executescript(file.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO posts (title, content) VALUES (?,?)", ('Post 1', 'Content for Post 1'))
cursor.execute("INSERT INTO posts (title, content) VALUES (?,?)", ('Post 2', 'Content for Post 2'))
cursor.execute("INSERT INTO posts (title, content) VALUES (?,?)", ('Post 3', 'Content for Post 3'))

connection.commit()
cursor.close()
