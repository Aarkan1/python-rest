# documentation:
# https://sanic.readthedocs.io/en/latest/index.html

# installation:
# pip install sanic

# start: 
# create virtual env: 
#   
# py main.py

from sanic import Sanic, response as res
from sanic.exceptions import NotFound
from sanic_cors import CORS
import time # to get unix timestamp

app = Sanic(__name__)
CORS(app) # enable cors on all origins

@app.get("/hello")
def read_root(req):
    return res.json({"Hello": "World"})

@app.get("/items/<item_id:int>")
def read_item(req, item_id):
    return res.json({"item_id": item_id, "q": q})

# route to get all todos
@app.get('/rest/todos')
async def get_todos(req):
    from database import getTodos

    return res.json(await getTodos())

# posting new todo
@app.post('/rest/todos')
async def post_todo(req):
    from database import createTodo

    # get body from req.json
    todo = req.json

    todo['timestamp'] = time.time()
    todo['id'] = await createTodo(todo)

    return res.json(todo)

@app.get('/rest/todos/<todo_id:int>')
async def get_todo_by_id(req, todo_id):
    from database import getTodoById

    return res.json(await getTodoById(todo_id))

@app.put('/rest/todos/<todo_id:int>')
async def put_todo_by_id(req, todo_id):
      # Handle UPDATE request
      return res.text('OK')

@app.delete('/rest/todos/<todo_id:int>')
async def delete_todo_by_id(req, todo_id):
    from database import deleteTodoById

    await deleteTodoById(todo_id)
    return res.text('OK')

# prevent mimetype errors from static files
import mimetypes
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('text/javascript', '.js')

# serve static files
app.static("/", "./www",)

# use 404 fallback (index.html) to handle SPA
@app.exception(NotFound)
async def ignore_404s(request, exception):
    return await res.file('./www/index.html')

# start server
if __name__ == "__main__":
  app.run(port=5000)