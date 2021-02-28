# documentation:
# https://www.encode.io/databases/

# installation:
# pip install databases[sqlite]

from databases import Database
db = Database('sqlite:awesome-todos.db')

# helper functions
async def get(query, values = {}):
    rows = await db.fetch_all(query=query, values=values)
    dicts = []
    for row in rows:
        dicts.append(dict(row))
    return dicts

async def run(query, values = {}):
    return await db.execute(query=query, values=values)

# CRUD functions
async def getTodos():
    return await get('SELECT * FROM todos')

async def getTodoById(id):
    todos = await get('SELECT * FROM todos WHERE id = :id', { "id": id })
    return todos[0] if todos else None

async def deleteTodoById(id):
    return await run('DELETE FROM todos WHERE id = :id', { "id": id })

async def createTodo(todo):
    q = 'INSERT INTO todos(text, timestamp) VALUES(:text, :timestamp)'
    return await run(q, { "text": todo['text'], "timestamp": todo['timestamp'] })