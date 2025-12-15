token = "8369459856:AAHDdO4DjtErKQppxxDYugMxrkFOkrewP2o" # тестовый

import sqlite3

def make_a_db():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users (
                    id INTEGER PRIMARY KEY,
                    acces_level INTEGER,
                    points INTEGER  
                )
                ''')
    connection.commit()
    connection.close()

make_a_db()

def check_db(id):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id, acces_level, points FROM Users WHERE id = ?", (id,))
    result = cursor.fetchall()
    connection.close()
    if len(result) == 0:
        return False
    else:
        return result
        
    

def db_add(id):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    if not check_db(id):
        cursor.execute("INSERT INTO Users (id, acces_level, points) VALUES (?, ?, ?) ", (id, 1, 1,))
        print("Added a User")
        connection.commit()
        connection.close()
        return check_db(id)
    else:
        connection.close()
        print("Already Exists")
        return check_db(id)


    
print(check_db("123"))
print(db_add("123"))
print(db_add("123"))

