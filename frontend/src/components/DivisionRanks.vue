<template>
  <div>
    <md-list>
      <md-list-item>
        <md-icon>move_to_inbox</md-icon>
        <span class="md-list-item-text">Inbox</span>
      </md-list-item>

    </md-list>
    <router-link :to="{ name: 'DivisionList'}">All divisions</router-link>
  </div>
</template>

<script>
import { divisionService } from '../services/DivisionService'

export default {
  name: 'DivisionList',
  data () {
    return {
      title: 'A list of all divisions'
    }
  },
  created() {
    console.log()
    divisionService.get().then(dbs => { this.divisions = divisionService.divisions })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
