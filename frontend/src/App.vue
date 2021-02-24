<template>
  <Navbar />
  <router-view />
</template>

<script>
import Navbar from './components/Navbar.vue'

export default {
  name: 'App',
  components: {
    Navbar
  },
  created() {
    this.$store.dispatch('initTodos')
  }
}
</script>
