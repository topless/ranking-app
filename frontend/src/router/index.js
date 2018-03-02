import Vue from 'vue'
import Router from 'vue-router'
import DivisionList from '@/components/DivisionList'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'DivisionList',
      component: DivisionList
    },
    {
      path: '/hello',
      name: 'HelloWorld',
      component: HelloWorld
    }
  ]
})
