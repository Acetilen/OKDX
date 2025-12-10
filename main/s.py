token = "8369459856:AAHDdO4DjtErKQppxxDYugMxrkFOkrewP2o" # тестовый

import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
               id INTEGER PRIMARY KEY,
               points INTEGER)
               ''')
cursor.execute('INSERT INTO Users(id,points) VALUES (?,?)', ('1', '20'))
connection.commit()
connection.close()




