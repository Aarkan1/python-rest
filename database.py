# https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
import sqlite3
from flask import g

# add db to the app context
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('awesome-todos.db')
    
    # Easy Querying by converting rows to dictionaries
    def make_dicts(cursor, row):
        return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

    db.row_factory = make_dicts
    return db

def query(query, args=()):
    cur = get_db().cursor()
    cur.execute(query, args)
    return cur.fetchall()

def insert(query, args=()):
    cur = get_db().cursor()
    cur.execute(query, args)
    get_db().commit()
    return cur.lastrowid

def delete(query, args=()):
    cur = get_db().cursor()
    cur.execute(query, args)
    get_db().commit()

def getTodos():
    return query('SELECT * FROM todos')

def getTodoById(id):
    todos = query('SELECT * FROM todos WHERE id = ?', (id,))
    return todos[0] if todos else None

def deleteTodoById(id):
    query = 'DELETE FROM todos WHERE id = ?'
    cur = get_db().cursor()
    cur.execute(query, (id,))
    get_db().commit()

def createTodo(todo):
    query = 'INSERT INTO todos(text, timestamp) VALUES(?, ?)'
    return insert(query, [todo['text'], todo['timestamp']])