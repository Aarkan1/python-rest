<template>
  <div v-for="todo of todos" :key="todo.text">
    <h3>{{ todo.text }}<span @click="deleteTodo(todo.id)">🗑️</span></h3>
    <p>{{ new Date(todo.timestamp * 1000).toLocaleString() }}</p>
  </div>
</template>

<script>
export default {
  computed: {
    todos() {
      return this.$store.state.todos
    }
  },
  methods: {
    async deleteTodo(id) {
      let res = await fetch('/rest/todos/' + id, {
        method: 'DELETE'
      })

      res.ok && this.$store.commit('deleteTodo', id)
    }
  }
}
</script>

<style scoped>
  h3, p {
    margin: 0;
  }

  div {
    margin-top: 15px;
  }

  span {
    cursor: pointer;
  }
</style>