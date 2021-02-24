import { createStore } from 'vuex'

const state = {
    todos: []
}

const mutations = {
    setTodos(state, todos) {
        state.todos = todos
    },
    appendTodo(state, todo) {
        state.todos.push(todo)
    },
    deleteTodo(state, id) {
        state.todos = state.todos.filter(todo => todo.id !== id)
    }
}

const actions = {
   async initTodos(store) {
        let todos = await fetch('/rest/todos')
        todos = await todos.json()
        console.log(todos);

        store.commit('setTodos', todos)
   }
}

export default createStore({
    state, 
    mutations, 
    actions
})