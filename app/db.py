from flask import current_app, g
from flask_pymongo import PyMongo


def get_db():
    if 'db' not in g:
        g.db = PyMongo(current_app, uri=current_app.config['DATABASE_URI']).db
    return g.db


