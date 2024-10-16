''' Module for database connection '''

from flask import g
from pymysql import connect, cursors

from src.util import config_util

def init_db(app):
    ''' Initializes database functionality by calling the close_db function
        after every request. '''
    app.teardown_appcontext(close_db)

def get_db():
    ''' Returns the database connection. If it doesnt exist yet, it is created
    first.
    Returns:
        pymysql.connections.Connection -- The database connection. '''
    if g:
        if "db" not in g:
            db_config = config_util.get("database")
            g.db = connect(host=db_config["hostname"],
                           user=db_config["username"],
                           password=db_config["password"],
                           db=db_config["database"],
                           cursorclass=cursors.DictCursor)
        return g.db

    db_config = config_util.get("database")
    return connect(host=db_config["hostname"],
                   user=db_config["username"],
                   password=db_config["password"],
                   db=db_config["database"],
                   cursorclass=cursors.DictCursor)

def close_db(_=None):
    ''' Closes the database connections, if any exist. This is usually called
        after a request is done. '''
    for key in ("db"):
        db_ = g.pop(key, None)
        if db_ is not None:
            db_.close()
