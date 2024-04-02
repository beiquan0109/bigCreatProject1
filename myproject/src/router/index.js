import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import pa from "../components/pa.vue";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'pa',
      component: pa
      // path: '/',
      // // name: 'HelloWorld',
      // name: 'Home',
      // // component: HelloWorld
      // component: Home
    }
  ]
})
