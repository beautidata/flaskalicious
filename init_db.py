import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('what is flask?', 'flask is a flexible web server gateway interface (wsgi) framework for python. \n flask is flexible.')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('why flask?', 'flask is lightweight, and using it requires few dependencies. flask templates are generated in jinja2.')
            )

connection.commit()
connection.close()