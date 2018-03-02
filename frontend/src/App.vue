<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',

  // Fetches posts when the component is created.
  created() {
    axios.get('api/v1/sample')
      .then(response => {
        console.log('Got it ', response.data)
      })
      .catch(e => {
        console.err(e)
      })
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
