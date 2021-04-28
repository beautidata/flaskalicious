# http://flask.pocoo.org/docs/1.0/tutorial/database/
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            "sqlite.db", detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))
    
    #cur = db.cursor()

    db.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('what is flask?', 'flask is a flexible web server gateway interface (wsgi) framework for python. \n flask is flexible.')
            )

    db.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('why flask?', 'flask is lightweight, and using it requires few dependencies. flask templates are generated in jinja2.')
            )

    db.commit()
    db.close()

@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)