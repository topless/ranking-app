<template>
  <div class="page-container">
    <div class="md-layout md-alignment-top-center">
      <img src="../assets/UFC_logo.svg">
    </div>

    <div class="md-layout md-alignment-top-center">
      <h2>{{title}}</h2>
    </div>

    <div class="md-layout">
      <md-list class="md-layout-item">
        <md-list-item v-for="division of divisions" :key="division.key" v-if="division.is_male">
          <md-button class="md-raised" :to="{ name: 'DivisionRanks'}">
            {{division.name}} - {{division.weight}}
          </md-button>
        </md-list-item>
      </md-list>

      <md-list class="md-layout-item">
        <md-list-item v-for="division of divisions" :key="division.key" v-if="!division.is_male">
          <md-button class="md-raised" :to="{ name: 'DivisionRanks'}">
            {{division.name}} - {{division.weight}}
          </md-button>
        </md-list-item>
      </md-list>
    </div>

    <ul v-if="errors && errors.length">
      <li v-for="error of errors" :key="error.message">
        {{error.message}}
      </li>
    </ul>
  </div>
</template>

<script>
import { divisionService } from '../services/DivisionService'

export default {
  name: 'DivisionRanks',
  data() {
    return {
      title: 'UFC divisions',
      p4p: {},
      divisions: [],
      errors: []
    }
  },
  created() {
    divisionService.get().then(dbs => { this.divisions = divisionService.divisions })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
