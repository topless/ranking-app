<template>
  <div>
    <img src="../assets/UFC_logo.svg">
    <h2>{{ msg }}</h2>
    <ul>
      <li>first item</li>
      <li>item number two</li>
      <li>more items</li>
    </ul>
    <router-link :to="{ name: 'DivisionRanks'}">Ranks</router-link>
  </div>
</template>

<script>
export default {
  name: 'DivisionRanks',
  data () {
    return {
      msg: 'A list of all UFC divisions'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
