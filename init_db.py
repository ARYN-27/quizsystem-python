import sqlite3

connection = sqlite3.connect('quizsystem_database.db')


with open('quiz_schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()



connection.commit()
connection.close()