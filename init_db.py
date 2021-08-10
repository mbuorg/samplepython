import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO hospital (name, address, phone) VALUES (?, ?, ?)",
            ('Apollo Hospital', 'Jaynagar 4th Block', '9780383824')
            )

connection.commit()
connection.close()
