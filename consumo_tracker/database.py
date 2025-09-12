import sqlite3

connection = sqlite3.connect("consuming.db")
cursor = connection.cursor()

# print(conn)
# print(cursor)

cursor.executescript('''
    DROP TABLE water_consuming;
    CREATE TABLE IF NOT EXISTS consuming(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        month TEXT NOT NULL,
        value INTEGER NOT NULL
    )                   
''')

connection.commit()
connection.close()
