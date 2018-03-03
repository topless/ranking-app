import Vue from 'vue'
import Router from 'vue-router'
import DivisionList from '@/components/DivisionList'
import DivisionRanks from '@/components/DivisionRanks'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'DivisionList',
      component: DivisionList
    },
    {
      path: '/ranks',
      name: 'DivisionRanks',
      component: DivisionRanks
    }
  ]
})
