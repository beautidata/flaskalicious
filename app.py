from flask import Flask, render_template, make_response
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/<page_name>')
def page_not_found(page_name):
    response = make_response('The page named %s was not found.' % page_name, 404)
    return response

if __name__ == '__main__':
    app.run(debug=True)