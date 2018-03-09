<template>
  <div class="container">
    <md-content class="title">
      <img src="../assets/UFC_logo.svg">
    </md-content>

    <md-content>
      <md-list>
        <!-- <md-list-item hidden>
          <md-button class="md-raised" :to="{ name: 'DivisionRanks'}">
            Pound for Pound
          </md-button>
        </md-list-item>
         -->
        <md-divider></md-divider>
        <md-list-item header><h3>Men</h3></md-list-item>
        <md-list-item v-for="division of divisions" :key="division.key" v-if="division.is_male">
          <md-button class="md-raised" :to="{ name: 'DivisionRanks', params: {name: division.name, isMale: division.is_male}}">
            {{division.name | divisionTitle}}
          </md-button> {{division.weight}} lbs
        </md-list-item>

        <md-divider></md-divider>
        <md-list-item header><h3>Women</h3></md-list-item>
        <md-list-item v-for="division of divisions" :key="division.key" v-if="!division.is_male">
          <md-button class="md-raised" :to="{ name: 'DivisionRanks', params: {name: division.name, isMale: division.is_male}}">
            {{division.name | divisionTitle}}
          </md-button> {{division.weight}} lbs
        </md-list-item>
      </md-list>
    </md-content>
  </div>
</template>

<script>
import { divisionService } from '../services/DivisionService'
import Vue from 'vue'

Vue.filter('divisionTitle', (value) => {
  return value.replace('_', ' ').toLowerCase()
})

export default {
  name: 'DivisionRanks',
  data() {
    return {
      divisions: [],
      errors: []
    }
  },
  created() {
    divisionService.get().then(dbs => { this.divisions = divisionService.divisions })
  }
}
</script>

<style lang="scss" scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  .md-content, .md-list {
    padding: 16px;
    background-color: transparent;
  }
  .md-button {
    flex-grow: 2;
  }
}
</style>
