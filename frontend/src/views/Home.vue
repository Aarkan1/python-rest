<template>
  <div>
    <h1>Todos</h1>
      <form @submit.prevent="addTodo">
        <input v-model="todoText" type="text" placeholder="new todo">
        <button>Add</button>
      </form>
      <TodoList />
  </div>
</template>

<script>
import TodoList from '../components/TodoList.vue'

export default {
  components: {
    TodoList
  },
  data() {
    return {
      todoText: ''
    }
  },
  methods: {
    async addTodo() {
      let todo = await fetch('/rest/todos', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: this.todoText })
      })

      if(todo.ok) {
        todo = await todo.json()
        console.log(todo);
        this.$store.commit('appendTodo', todo)
      }


      this.todoText = ''
    }
  }
}
</script>

<style>

</style>