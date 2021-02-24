# https://flask.palletsprojects.com/en/1.1.x/quickstart/
# install Flask:
# pip install Flask

# start server:
# py main.py

# OR
# export FLASK_APP=main.py
# flask run

from flask import Flask, g, jsonify, render_template, request
from markupsafe import escape
import time

# prevent mimetype errors
import mimetypes
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('text/javascript', '.js')

# serve static folder and handle SPA (Single Page Application)
app = Flask(__name__, static_folder='www', template_folder='www', static_url_path='/')
import database

# on shutdown
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# dynamic route test
@app.route('/api/<username>')
def api_username(username):
    return 'User %s' % escape(username)

# dynamic route test
# with autoparsing to integer
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

# testroute for returning json
@app.route('/heartbeat')
def heartbeat():
    return jsonify({ 'status': 'healthy' })

# route to get all todos
# or posting new todo
@app.route('/rest/todos', methods=['GET', 'POST'])
def get_todos():
    from database import getTodos, createTodo

    res = {}

    if request.method == 'POST':
        # get json data from post object
        body = request.get_json() 
        todo = {
            'text': body['text'],
            'timestamp': time.time()
        }

        id = createTodo(todo)
        res = todo
        res['id'] = id

    else:
        res = getTodos()

    return jsonify(res)

# routes to either
# GET - get a todo by id
# PUT - update todo by id
# DELETE - delete todo by id
@app.route('/rest/todos/<int:todo_id>', methods=['GET', 'PUT', 'DELETE'])
def update_todos(todo_id):
    from database import getTodoById, deleteTodoById

    if request.method == 'GET':
        return jsonify(getTodoById(todo_id))
    elif request.method == 'PUT':
        pass  # Handle UPDATE request
    elif request.method == 'DELETE':
        deleteTodoById(todo_id)
        return 'OK'

# Handle SPA
@app.route('/')
def spa():
    return render_template("index.html")

# Let frontend deal with different routes
@app.errorhandler(404)
def page_not_found(error):
    return render_template("index.html")

# test function to try sqlite
def use_get_db_outside_of_context():
    from database import get_db
    with app.app_context():
        cur = get_db().cursor()
        cur.execute('SELECT * FROM todos')
        print(cur.fetchall())
        
# start server
if __name__ == "__main__":
    # app.debug = True
    app.run(port = 5000)