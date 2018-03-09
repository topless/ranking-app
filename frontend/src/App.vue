<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style lang="scss">
@import "~vue-material/dist/theme/engine";
@include md-register-theme("default", (
  theme: dark
));
@import "~vue-material/dist/theme/all";

#app {
  padding-top: 64px;
}
</style>
