from flask import Flask, render_template, make_response, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort
from configparser import ConfigParser

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)
config = ConfigParser()
config.readfp(open('settings.ini'))
app.config['SECRET_KEY'] = config.get('flaskalicious', 'secret_key')

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/<page_name>')
def page_not_found(page_name):
    response = make_response('The page named %s was not found.' % page_name, 404)
    return response

@app.route('/create', methods=('GET', 'POST'))
def create():
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)