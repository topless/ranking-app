<template>
  <div>
    <h2>{{ title }}</h2>
    <ul>
      <li>first item</li>
      <li>item number two</li>
      <li>more items</li>
    </ul>
    <router-link to="hello">back to World</router-link>
  </div>
</template>

<script>
export default {
  name: 'This is a list example',
  data () {
    return {
      title: 'A list of all divisions'
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
